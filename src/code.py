import time

import board
import neopixel

import colors
from models import MultiGradient, Map, Solid, Triangle, Reverse
from animations import Rotate, Pulsate
from renderer import Renderer

# Setup neopixel strip
PIXELS_PIN = board.GP28
PIXELS_COUNT = 50
BRIGHTNESS = 0.5
ORDER = neopixel.RGB

strip = neopixel.NeoPixel(PIXELS_PIN, PIXELS_COUNT, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER)

strip.fill(colors.WHITE)
strip.show()
time.sleep(0.2)

gradient = MultiGradient("Gradient rainbow", [colors.RED, colors.ORANGE, colors.YELLOW,
                                                colors.GREEN, colors.BLUE, colors.VIOLET, colors.RED])
triangle = Triangle("Triangle WHITE", 0.1, 1.0, colors.WHITE)
rotate = Rotate("Rotation", 5000, triangle)
pulsate = Pulsate("Pulsate", 0.1, 1.0, 1000, 1000, rotate)
reverse = Reverse("Reverse", gradient)

renderer = Renderer(PIXELS_COUNT, reverse)

while True:
    pixels = renderer.loop()
    for i in range(len(pixels)):
        strip[i] = pixels[i]
    strip.show()
    time.sleep(.001)


# std::shared_ptr<Model> makeDarkCrystal() {
#   return makeCrystal(0xff00d0, 5.0, 0xff00d0, 8.0, 0xff00d0, 7.0);
# }
#
# std::shared_ptr<Model> makeCrystal(
#     Color upperColor, float upperPeriodSec,
#     Color middleColor, float middlePeriodSec,
#     Color lowerColor, float lowerPeriodSec) {
#
#   auto upperTriangle = std::make_shared<Triangle>("crystal upper color", 0.6, 1.0, upperColor);
#   std::shared_ptr<Model> upperPulsate = upperTriangle;
#   if (upperPeriodSec <= 10.0) {
#     upperPulsate = std::make_shared<Pulsate>("crystal upper pulsate", 0.3, 1.0, upperPeriodSec/2.0, upperPeriodSec/2.0, upperTriangle);
#   }
#
#   auto middleTriangle = std::make_shared<Triangle>("crystal middle color", 0.3, 0.7, middleColor);
#   std::shared_ptr<Model> middlePulsate = middleTriangle;
#   if (middlePeriodSec <= 10.0) {
#     middlePulsate = std::make_shared<Pulsate>("crystal middle pulsate", 0.4, 1.0, middlePeriodSec/2.0, middlePeriodSec/2.0, middleTriangle);
#   }
#
#   auto lowerTriangle = std::make_shared<Triangle>("crystal lower color", 0.0, 0.4, lowerColor);
#   std::shared_ptr<Model> lowerPulsate = lowerTriangle;
#   if (lowerPeriodSec <= 10.0) {
#     lowerPulsate = std::make_shared<Pulsate>("crystal lower pulsate", 0.3, 1.0, lowerPeriodSec/2.0, lowerPeriodSec/2.0, lowerTriangle);
#   }
#
#   auto sum = std::make_shared<Add>("sum", upperPulsate, middlePulsate);
#   sum = std::make_shared<Add>("sum", sum, lowerPulsate);
#
#   return sum;
# }
