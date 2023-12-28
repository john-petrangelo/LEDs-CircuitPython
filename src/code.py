import time

import board

from colors import WHITE
from luminaria import colors
from luminaria.models import MultiGradient, Solid
from luminaria.animations import Rotate
from luminaria.renderer.circuitpython_neopixel_renderer import Renderer

# Setup neopixel sequence
print("Initializing pixels")
PIXELS_PIN = board.GP28
PIXELS_COUNT = 50
BRIGHTNESS = 1.0
pixels = Renderer(PIXELS_PIN, PIXELS_COUNT, brightness=BRIGHTNESS)

# Flash the pixels white for a short time
pixels.model = Solid("Solid white", WHITE)
pixels.render()
time.sleep(0.2)

# Set up the model for the pixels
print("Setting up lighting model")
gradient = MultiGradient("Gradient rainbow",
                         [colors.RED, colors.ORANGE, colors.YELLOW, colors.GREEN, colors.BLUE, colors.VIOLET,
                          colors.RED])
rotate = Rotate("Rotation", 2500, gradient)
pixels.model = rotate

print("Starting loop")
while True:
    pixels.render()
    time.sleep(.010)
