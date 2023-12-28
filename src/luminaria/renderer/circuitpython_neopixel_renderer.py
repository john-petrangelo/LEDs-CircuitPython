import time

import neopixel
from microcontroller import Pin

from models import Model


# PIXELS_PIN = board.GP28
# ORDER = neopixel.RGB


class Renderer:
    """
      A class responsible for rendering a model onto NeoPixel LEDs.

      :param pixels_pin: The pin to which the NeoPixel LED strip is connected.
      :param pixels_count: The number of NeoPixel LEDs in the strip.
      :param pixels_order: The color order of the NeoPixel LEDs (default: neopixel.RGB).
      :param brightness: The brightness of the NeoPixel LEDs, ranging from 0.0 to 1.0 (default: 1.0).

      :method render: Renders the current state of the assigned model onto the NeoPixel LEDs.
      :method reset: Resets the reference time for model rendering to the current time.
      """

    def __init__(self, pixels_pin: Pin, pixels_count: int, *, pixels_order: str = neopixel.RGB, brightness: float = 1.0):
        self._pixels = neopixel.NeoPixel(pixels_pin, pixels_count, pixel_order=pixels_order,
                                         brightness=brightness, auto_write=False)
        self._brightness = brightness
        self._start_time = time.monotonic_ns() // 1000000
        self._model = None

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model: Model):
        self._model = new_model

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness: float):
        self._brightness = brightness

    def render(self):
        """
        Render the model at the current time and updates the LED lights accordingly.
        """

        # If there's no model then there is nothing to render.
        if self._model is None:
            return

        # Update the current state of the model to match the current time.
        absolute_now_ms = time.monotonic()*1000
        relative_now_ms = absolute_now_ms - self._start_time
        self._model.update(relative_now_ms)

        # Now set the color for each pixel
        for i in range(self._pixels.n):
            pos = i / (self._pixels.n - 1)
            color = self._model.render(pos)
            self._pixels[i] = color

        # Write the new colors to the LEDs
        self._pixels.show()

    def reset(self):
        """
        Reset the reference time for model rendering to now
        """
        self._start_time = time.monotonic_ns() // 1000000
