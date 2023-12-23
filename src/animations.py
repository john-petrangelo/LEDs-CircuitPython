import colors
from models import Model, Add, Triangle


def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Pulsate(Model):
    """
    Adjusts the brightness of the underlying model from dimmest to brightest and back again.
    For example, the brightness may increase from 20% to 100% over 3 seconds and then dim
    back down to 20% over 1.5 seconds.

    Requires underlying model
    Position independent, time dependent
    """
    dimness = 0.0

    def __init__(self, name: str, dimmest: float, brightest: float, dim_ms: float, brighten_ms: float,
                 model: Model):
        """
        :param name: Name of this model, shown in debug messages
        :param dimmest: The min brightness (0.0 - 1.0)
        :param brightest: The max brightness (0.0 - 1.0)
        :param dim_ms: Dimming period in milliseconds
        :param brighten_ms: Brightening period in milliseconds
        :param model: The underlying model to be pulsated
        """
        self.dimmest = dimmest
        self.brightest = brightest
        self.dim_ms = dim_ms
        self.brighten_ms = brighten_ms
        self.period_ms = self.dim_ms + self.brighten_ms
        self.model = model

        super().__init__(name)

    def update(self, timestamp_ms: float):
        mod_timestamp_ms = timestamp_ms % self.period_ms
        if mod_timestamp_ms < self.brighten_ms:
            # We're getting brighter
            self.dimness = map_value(mod_timestamp_ms, 0.0, self.brighten_ms, self.brightest, self.dimmest)
        else:
            # We're getting dimmer
            self.dimness = map_value(mod_timestamp_ms, self.brighten_ms, self.period_ms, self.dimmest, self.brightest)

        self.model.update(timestamp_ms)

    def render(self, pos: float):
        old_color = self.model.render(pos)
        new_color = colors.fade(old_color, self.dimness)
        return new_color


# Rotate
#

class Rotate(Model):
    """
    An animation that rotates or shifts lights to the left or right.
    Wraps around so that once a color reaches the end, then it wraps around.
    The speed of rotation is given as the period of a cycle in ms. A period
    of zero is stopped. Positive speed rotates up, negative speed rotates down.
    """
    rotation_offset = 0.0
    prev_timestamp_ms = 0

    def __init__(self, name: str, period_ms: float, model: Model):
        """
        :param name: Name of this model, shown in debug messages
        :param period_ms:
        :param model:
        """
        self.period_ms = period_ms
        self.model = model
        super().__init__(name)

    def update(self, timestamp_ms: int):
        # New timestamp, calculate the new offset
        delta_time_ms = timestamp_ms - self.prev_timestamp_ms
        self.prev_timestamp_ms = timestamp_ms

        # How far should we rotate given the time delta. Handle wrapping to keep
        # offset between 0.0 and 1.0.
        delta_pos = -delta_time_ms / self.period_ms
        self.rotation_offset = (self.rotation_offset + delta_pos) % 1.0

        if self.rotation_offset < 0.0:
            self.rotation_offset += 1.0

        # Update the wrapped model as well.
        self.model.update(timestamp_ms)

    def render(self, pos: float):
        # If there's no predecessor, then there's nothing to rotate. Bail out.
        if not self.model:
            return colors.RED

        # Add the offset to the position, then correct for wrap-around
        rotated_pos = (pos + self.rotation_offset) % 1.0
        if rotated_pos < 0.0:
            rotated_pos += 1.0

        return self.model.render(rotated_pos)

    def set_period(self, new_period_ms: float):
        """ Set the period of one rotation cycle in ms """
        self.period_ms = new_period_ms

    def set_model(self, new_model: Model):
        """ Set the model to be rotated """
        self.model = new_model


def make_crystal(upper_color: tuple, upper_period_ms: float,
                 middle_color: tuple, middle_period_ms: float,
                 lower_color: tuple, lower_period_ms: float):
    upper_model = Triangle("crystal upper color", 0.6, 1.0, upper_color)
    middle_model = Triangle("crystal middle color", 0.3, 0.7, middle_color)
    lower_model = Triangle("crystal lower color", 0.0, 0.4, lower_color)

    if upper_period_ms <= 10 * 1000:
        print("Adding pulsate to upper crystal model")
        upper_model = Pulsate("crystal upper pulsate", 0.3, 1.0,
                              upper_period_ms / 2, upper_period_ms / 2, upper_model)
    if upper_period_ms <= 10 * 1000:
        middle_model = Pulsate("crystal middle pulsate", 0.4, 1.0,
                               middle_period_ms / 2, middle_period_ms / 2, middle_model)
    if upper_period_ms <= 10 * 1000:
        lower_model = Pulsate("crystal lower pulsate", 0.3, 1.0,
                              lower_period_ms / 2, lower_period_ms / 2, lower_model)

    return Add("crystal sum", [upper_model, middle_model, lower_model])


def make_dark_crystal():
    color = (255, 0, 208)
    return make_crystal(color, 5000, color, 8000, color, 7000)
