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


def same(c1: tuple, c2: tuple, allowed_delta: float = 0.001) -> bool:
    """
    Check if two color tuples are nearly identical within a specified delta.

    Parameters:
    - `c1` (tuple): The first color tuple to compare.
    - `c2` (tuple): The second color tuple to compare.
    - `allowed_delta` (float, optional): The maximum allowed difference for each channel.
      Defaults to 0.001.

    Returns:
    - bool: True if the color tuples are nearly identical, False otherwise.

    The function checks if each channel (red, green, blue) of the two color tuples `c1` and `c2` are nearly equal
    within the specified `allowed_delta`.

    Usage:
    ```python
    color1 = (255, 0, 0)
    color2 = (255, 0, 0)
    if same(color1, color2):
        print("Colors are nearly identical.")
    ```

    Note:
    - The function uses the specified `allowed_delta` to account for potential floating-point inaccuracies in color representations.
    - Adjust the `allowed_delta` parameter based on the precision requirements of your color comparison.
    """
    for channel in zip(c1, c2):
        if abs(channel[0] - channel[1]) > allowed_delta:
            return False

    return True


def blend(c1: tuple, c2: tuple, ratio: float) -> tuple:
    """
    Blend two colors resulting in a new color. The blend is expressed as a ratio of the blend between
    the two colors. 0 means all first color, 100 means all second color, 50 means 50% of each.

    :param c1: First color
    :param c2: Second color
    :param ratio: Ratio of second color to first color [0.0 - 1.0]
    :return: blended color
    """
    if len(c1) != 3 or len(c2) != 3:
        return GRAY

    red = c1[0] + (c2[0] - c1[0]) * ratio
    green = c1[1] + (c2[1] - c1[1]) * ratio
    blue = c1[2] + (c2[2] - c1[2]) * ratio
    return red, green, blue


def fade(c: tuple, ratio: float):
    """
    Fade the color towards black.
    :param c: The color
    :param ratio: Amount of blackness, 0.0 = black, 1.0 = full color, 0.5 = halfway to black
    :return: faded color
    """
    return blend(BLACK, c, ratio)


def add(*colors: tuple):
    """
    Add colors together, constraining each color component to valid range
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
