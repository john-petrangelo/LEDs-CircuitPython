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


def add(*colors: tuple):
    """
    Add two colors together, constraining each component to maximum value of 255
    :param colors: colors to add together
    :return: sum of colors
    """
    if not colors:
        return BLACK
    sum_red, sum_green, sum_blue = map(sum, zip(*colors))

    # Return the resulting sum, constraining value to be between 0 and 255
    return (max(min(255, sum_red), 0),
            max(min(255, sum_green), 0),
            max(min(255, sum_blue), 0))
