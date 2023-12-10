import colors


class Model:
    def __init__(self, name):
        self.name = name

    # Updates the model to the current timestamp. Models that change with time (animations)
    # will need to implement this function. A default implementation is provided for static
    # models that do not change with time.
    def update(self, timestamp: float):
        pass

    # Returns the color that should be displayed at the specified pos at the current time.
    def render(self, pos: float):
        pass

    # Returns the name of this model, provided in the constructor.
    def getname(self):
        return self.name


# Set a solid color pattern
class Solid(Model):
    def __init__(self, name, color: tuple):
        super().__init__(name)
        self.color = color

    def render(self, pos: float):
        return self.color


# Set a gradient color pattern from one color to another color
class Gradient(Model):
    def __init__(self, name: str, a: tuple, b: tuple):
        super().__init__(name)
        self.a = a
        self.b = b

    def render(self, pos: float):
        return colors.blend(self.a, self.b, int(100 * pos))
