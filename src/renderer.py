from models import Model
import time


class Renderer:
    def __init__(self, pixels_count: int, model: Model):
        self.pixels_count = pixels_count
        self.model = model
        self.start_time = time.monotonic_ns()

    # C++ signature: void loop(int numPixels, std::function<void(int, Color)> setPixel);
    # setPixel is a function to set the color of a pixel
    def loop(self):
        # If there's no model then there is nothing to do.
        if self.model is None:
            return

        # Update the current state of the model to match the current time.
        absolute_now = time.monotonic_ns()
        relative_now = (absolute_now - self.start_time) // 1000
        self.model.update(relative_now)

        # Now figure out the color for each pixel
        pixels = []
        for i in range(self.pixels_count):
            pos = i / (self.pixels_count - 1)
            color = self.model.render(pos)
            pixels.append(color)

        return pixels
