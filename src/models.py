import colors


class Model:
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
        super().__init__(name)
        self.color = color

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
