import math

import colors
import utils


class Model:
    """
    To be documented...
    """
    def __init__(self, name: str):
        """
        :param name: Name of this model, shown in debug messages
        """
        self.name = name

    def update(self, timestamp_ms: float):
        """
        Updates the model to the specified timestamp. Usually a renderer will get the time
        of rendering and use the same time stamp to update all models.

        Models that change with time (animations) will need to implement this function.
        Models that do not change with time do not need to implement this method.

        :param timestamp_ms: the time in milliseconds to which to adjust the model
        """
        pass

    def render(self, pos: float):
        """
        Returns the color that should be displayed at the specified pos at the current time.

        :param pos: position of the pixel to be rendered (0.0 - 1.0)
        :return: color
        """
        return colors.BLACK


class Solid(Model):
    """
    Set a solid color pattern
    """
    def __init__(self, name, color: tuple):
        """
        :param name: Name of this model, shown in debug messages,
        :param color: Color of this solid model
        """
        self.color = color
        super().__init__(name)

    def render(self, pos: float):
        return self.color


class Gradient(Model):
    """
    Set a gradient color pattern from one color to another color
    """
    def __init__(self, name: str, c1: tuple, c2: tuple):
        """
        :param name: Name of this model, shown in debug messages
        :param c1: First color of the gradient
        :param c2: Second color of the gradient
        """
        self.c1 = c1
        self.c2 = c2
        super().__init__(name)

    def render(self, pos: float):
        return colors.blend(self.c1, self.c2, int(100 * pos))


class MultiGradient(Model):
    """
    Set a gradient color pattern. The number of defined color points is variable.
    """
    def __init__(self, name: str, color_list: list):
        self.color_list = color_list
        super().__init__(name)

    def render(self, pos: float):
        color_pos = pos * (len(self.color_list)-1)
        lower = math.floor(color_pos)
        upper = math.ceil(color_pos)

        # Linearly interpolate from the lower color to the upper color. If same, quick return.
        if upper == lower:
            return self.color_list[lower]

        ratio = (color_pos - lower) / (upper - lower)
        return colors.blend(self.color_list[lower], self.color_list[upper], int(100 * ratio))


class Map(Model):
    """
    Map a model into a smaller range
    Map offers a powerful way to help created complex models using composition of simpler models. Models typically
    cover a range of 0.0 - 1.0. With Map, you can render another Model into a smaller range.
    For example, creating a Map(gradient, 0.8, 0.9, 0.0, 0.5) would create a new model with the first half
    the gradient squished into the 0.8 - 0.9 range of the resulting model.
    """
    def __init__(self, name: str, in_min, in_max, out_min, out_max, model: Model):
        self.in_min = in_min
        self.in_max = in_max
        self.out_min = out_min
        self.out_max = out_max
        self.model = model
        super().__init__(name)

    def update(self, timestamp_ms: float):
        self.model.update(timestamp_ms)

    def render(self, pos: float):
        if self.in_min <= pos <= self.in_max:
            out_pos = utils.map_value(pos, self.in_min, self.in_max, self.out_min, self.out_max)
            print(f"Map: {pos}->{out_pos}  in_min={self.in_min} in_max={self.in_max} out_min={self.out_min} out_max={self.out_max} ")
            return self.model.render(out_pos)

        # Everything outside the input range will be BLACK
        print(f"map {pos} outside")
        return colors.BLACK


class Triangle(Model):
    """
    Creates a range of colors from black to the specified color and then black again, with the
    full color at the midpoint of the range. Outside the range returns BLACK.
    """

    def __init__(self, name: str, range_min: float, range_max: float, color: tuple):
        self.range_min = range_min
        self.range_max = range_max
        self.color = color
        super().__init__(name)

    def render(self, pos: float):
        if pos < self.range_min or pos > self.range_max:
            return colors.BLACK

        mid_point = (self.range_min + self.range_max) / 2

        if pos <= mid_point:
            # Rising side of triangle
            ratio = 100 * utils.map_value(pos, self.range_min, mid_point, 0.0, 1.0)
            return colors.blend(colors.BLACK, self.color, ratio)
        else:
            # Falling side of triangle
            ratio = 100 * utils.map_value(pos, mid_point, self.range_max, 1.0, 0.0)
            return colors.blend(colors.BLACK, self.color, ratio)


class Reverse(Model):
    """
    Create a new model that is the reverse of the input model
    """

    def __init__(self, name: str, model: Model):
        self.model = model
        super().__init__(name)

    def update(self, timestamp_ms: float):
        self.model.update(timestamp_ms)

    def render(self, pos: float):
        return self.model.render(1.0 - pos)

# ##### IDEAS #####

#  Dim
#  Adjust the brightness of the color down by the provided percent
#
#  Constructors:
#    Dim(dimPercent, model) - dims all colors of the underlying model by dimPercent, expressed as 0.0-1.0
#
#  Requires input model
#  Position and time independent


#  Brighten
#  Increases the brightness of the color up by the provided percent, no R, G, or B will exceed 255
#  (Note: is this a new "Filter" category of models?)
#
#  Constructors:
#    Brighten(brightenPercent, model) - brightens all colors of the  model by brightenPercent, expressed as 0.0-1.0
#
#  Requires input model
#  Position and time independent


#  Firefly
#  A firefly (small light band? needs definition) flits around in a specified range with
#  some sort of speed parameters


#  Matrix
#  Green spots flow from one end of the strip to the other.
#  Can experiment with varying rates, sizes, brightnesses, hues.
#
#  Position and time dependent.


#  Blend
#  Blend two models together. Details TBD, but options include LERP, add, etc.
#
#  Requires two input models.
#  Position and time independent.


#  Blur
#  Performs some sort of convolution around a position to blur the colors.
#
#  Requires input model.
#  Position and time independent.


#  Lava lamp
#  Simulate a lava lamp.
#
#  Direction - up/down
#  Color

#  Warp core
#  Simulate a Star Trek warp core.
#
#  Direction - up/down?
#  Color?
#  Speed?


#  Jacob's ladder
#  Simulate the rising electrical arc of a Jacob's ladder.
#
#  Color?
#  Speed?
