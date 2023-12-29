import wx

from luminaria.animations import Rotate
from luminaria.colors import BLUE, GREEN, ORANGE, RED, VIOLET, YELLOW
from luminaria.models import MultiGradient
from luminaria.renderer.wx_renderer import Renderer

PIXELS_COUNT = 100
PIXEL_GAP_WIDTH = 10


class PixelDrawingPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self._renderer = None

    def on_paint(self, _):
        dc = wx.PaintDC(self)
        # self.draw_pixels(dc)
        self._renderer.render()

    def set_renderer(self, renderer: Renderer):
        self._renderer = renderer
        renderer.set_panel(self)


class PixelDrawingFrame(wx.Frame):
    def __init__(self, renderer: Renderer, window_width: int, window_height: int, *args, **kw):
        super().__init__(*args, **kw)

        # Set up the frame with size, position, and background color
        self.SetSize(window_width, window_height)
        self.Centre()
        self.SetBackgroundColour(wx.Colour(32, 32, 32))

        # Create the panel where the pixels will be drawn
        self.panel = PixelDrawingPanel(self)
        self.panel.set_renderer(renderer)

        # Set up a timer to update the pixels periodically
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(10) # ms

        # Start the show
        self.Refresh()
        self.Show(True)

    def on_timer(self, _):
        self.Refresh()


def calc_sizes():
    screen_width, screen_height = wx.GetDisplaySize()

    pixel_width = (screen_width - 20 - (PIXELS_COUNT + 1) * PIXEL_GAP_WIDTH) // PIXELS_COUNT
    pixel_width = min(96, pixel_width)
    window_width = (PIXELS_COUNT + 1) * PIXEL_GAP_WIDTH + PIXELS_COUNT * pixel_width
    return pixel_width, window_width


if __name__ == "__main__":
    # Create the wx app object
    app = wx.App(False)

    # Figure out window size as well as the size of the pixels to draw
    pixel_size, window_w = calc_sizes()
    print(f"pixel_size={pixel_size}  window_width={window_w}")

    # Set up the model for the pixels
    print("Setting up model")
    wx_renderer = Renderer(PIXELS_COUNT, pixel_size, PIXEL_GAP_WIDTH)
    gradient = MultiGradient("Gradient rainbow", [RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, RED])
    rotate = Rotate("Rotation", 2500, gradient)
    wx_renderer.model = rotate

    # Launch the app window
    print("Opening window")
    frame = PixelDrawingFrame(wx_renderer, window_w, pixel_size + 48, None, title="Pixels Animation Simulator")
    app.MainLoop()
