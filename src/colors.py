# Useful pre-defined colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 63, 0)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
VIOLET = (143, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


def blend(c1: tuple, c2: tuple, ratio: int) -> tuple:
    """
    Blend two colors resulting in a new color. The blend is expressed as a ratio of the blend between
    the two colors. 0 means all first color, 100 means all second color, 50 means 50% of each.

    :param c1: First color
    :param c2: Second color
    :param ratio: Ratio of second color to first color.
    :return: blended color
    """
    if len(c1) != 3 or len(c2) != 3:
        return GRAY

    red = c1[0] + (c2[0] - c1[0]) * ratio / 100
    green = c1[1] + (c2[1] - c1[1]) * ratio / 100
    blue = c1[2] + (c2[2] - c1[2]) * ratio / 100
    return red, green, blue


def fade(c: tuple, ratio: int):
    """
    Fade the color towards black. Ratio of 0 gives black, 100 gives color, 50 is halfway to black.
    :param c: The color
    :param ratio: Amount of blackness, 0 = black, 100 = full color, 50 = halfway to black
    :return: faded color
    """
    return blend(BLACK, c, ratio)


def add(c1: tuple, c2: tuple):
    """
    Add two colors together, constraining each component to 255 (max saturation)
    :param c1: first color
    :param c2: second color
    :return: sum of colors
    """
    if len(c1) != 3 or len(c2) != 3:
        return GRAY

    return (_constrain(c1[0] + c2[0], 0, 255),
            _constrain(c1[1] + c2[1], 0, 255),
            _constrain(c1[2] + c2[2], 0, 255))


def _constrain(n: int, min_val: int, max_val: int):
    """
    Constrain a value to lie in the specified range
    :param n: the value to be constrained
    :param min_val: minimum value allowed
    :param max_val: maximum value allowed
    :return: the constrained value, where min_val <= value <= max_value
    """
    return max(min(max_val, n), min_val)
