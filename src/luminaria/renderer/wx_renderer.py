import time

import wx

from luminaria.models import Model


class Renderer:
    """
      A class responsible for rendering a model in a wx Panel using wxPython.

      :param pixels_count: The number of pixels to light up
      :param pixel_size: The diameter of the pixels to render
      :param pixels_gap_width: The amount of horizontal space to leave between pixels
      """

    def __init__(self, pixels_count: int, pixel_size: int, pixels_gap_width: int):
        self._pixels_count = pixels_count
        self._pixel_size = pixel_size
        self._pixels_gap_width = pixels_gap_width
        self._start_time = time.monotonic_ns() // 1000000
        self._panel = None
        self._model = None

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model: Model):
        self._model = new_model

    def render(self):
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
        absolute_now_ms = time.monotonic()*1000
        relative_now_ms = absolute_now_ms - self._start_time
        self._model.update(relative_now_ms)

        # Now draw each pixel
        dc = wx.PaintDC(self._panel)
        for i in range(self._pixels_count):
            pos = i / (self._pixels_count - 1)
            color = self._model.render(pos)
            x = (i+1)*self._pixels_gap_width + i*self._pixel_size
            y = 10

            wx_color = wx.Colour(color[0], color[1], color[2])
            dc.SetBrush(wx.Brush(wx_color))
            dc.DrawCircle(x + self._pixel_size//2, y + self._pixel_size//2, self._pixel_size//2)

    def reset(self):
        """
        Reset the reference time for model rendering to now
        """
        self._start_time = time.monotonic_ns() // 1000000

    def set_panel(self, panel: wx.Panel):
        self._panel = panel
