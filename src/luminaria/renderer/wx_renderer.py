import time

import wx

from luminaria.models import Model

PIXEL_GAP_WIDTH = 10
PIXEL_MAX_WIDTH = 96


class Renderer:
    """
      A class responsible for rendering a model in a wx Panel using wxPython.

      :param pixels_count: The number of pixels to light up
      :param model: (optional) The model to render
      """
    def __init__(self, pixels_count: int, model: Model = None):
        self._pixels_count = pixels_count
        self._start_time = time.monotonic_ns() // 1000000
        self._model = model

        # Create the frame/window
        self._pixel_size, window_width = _calc_sizes(pixels_count)
        self._frame = PixelDrawingFrame(self, window_width, self._pixel_size + 48, None,
                                        title="Pixels Animation Simulator")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model: Model):
        self._model = new_model

    def render(self, panel: wx.Panel):
        """
        Render the model at the current time and updates the LED lights accordingly.
        """
        # If there's no model then there is nothing to render.
        if self._model is None:
            print("No model to render")
            return

        # If there's no model then there is nothing to render.
        if self._model is None:
            print("No panel to render to")
            return

        # Update the current state of the model to match the current time.
        absolute_now_ms = time.monotonic() * 1000
        relative_now_ms = absolute_now_ms - self._start_time
        self._model.update(relative_now_ms)

        # Now draw each pixel
        dc = wx.PaintDC(panel)
        for i in range(self._pixels_count):
            pos = i / (self._pixels_count - 1)
            color = self._model.render(pos)
            x = (i + 1) * PIXEL_GAP_WIDTH + i * self._pixel_size
            y = 10

            wx_color = wx.Colour(color[0], color[1], color[2])
            dc.SetBrush(wx.Brush(wx_color))
            dc.DrawCircle(x + self._pixel_size // 2, y + self._pixel_size // 2, self._pixel_size // 2)

    def reset(self):
        """
        Reset the reference time for model rendering to now
        """
        self._start_time = time.monotonic_ns() // 1000000


def _calc_sizes(pixels_count: int):
    screen_width, screen_height = wx.GetDisplaySize()

    pixel_width = (screen_width - 2 * PIXEL_GAP_WIDTH - (pixels_count + 1) * PIXEL_GAP_WIDTH) // pixels_count
    pixel_width = min(PIXEL_MAX_WIDTH, pixel_width)
    window_width = (pixels_count + 1) * PIXEL_GAP_WIDTH + pixels_count * pixel_width
    return pixel_width, window_width


class PixelDrawingFrame(wx.Frame):
    def __init__(self, renderer: Renderer, window_width: int, window_height: int, *args, **kw):
        super().__init__(*args, **kw)

        # Set up the frame with size, position, and background color
        self.SetSize(window_width, window_height)
        self.Centre()
        self.SetBackgroundColour(wx.Colour(32, 32, 32))

        # Create the panel where the pixels will be drawn
        self.panel = PixelDrawingPanel(self, renderer)

        # Set up a timer to update the pixels periodically
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(10)  # ms

        # Start the show
        self.Refresh()
        self.Show(True)

    def on_timer(self, _):
        self.Refresh()


class PixelDrawingPanel(wx.Panel):
    def __init__(self, parent: wx.Frame, renderer: Renderer):
        super().__init__(parent)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self._renderer = renderer

    def on_paint(self, _):
        self._renderer.render(self)
