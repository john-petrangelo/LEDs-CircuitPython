import wx

from luminaria.animations import Flame, Rotate
from luminaria.colors import BLUE, GREEN, ORANGE, RED, VIOLET, YELLOW
from luminaria.models import MultiGradient
from luminaria.renderer.wx_renderer import Renderer

PIXELS_COUNT = 24


if __name__ == "__main__":
    # Create the wx app object
    app = wx.App(False)

    # Set up the model defining the pixel colors
    print("Setting up model for rendering")
    # gradient = MultiGradient("Gradient rainbow", [RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, RED])
    # rotate = Rotate("Rotation", 1/10, gradient)
    # model = rotate

    model = Flame("Flame")

    wx_renderer = Renderer(PIXELS_COUNT, model)

    # Run the app
    print("App loop starting")
    app.MainLoop()
