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


# Blend the provided colors
# Ratio of the blend between a and b. 0 means all c1, 100 means all c1, 50 means 50% of each.
def blend(c1: tuple, c2: tuple, ratio: int):
    if len(c1) != 3 or len(c2) != 3:
        return GRAY

    red = c1[0] + (c2[0] - c1[0]) * ratio / 100
    green = c1[1] + (c2[1] - c1[1]) * ratio / 100
    blue = c1[2] + (c2[2] - c1[2]) * ratio / 100
    return red, green, blue


# Fade the color towards black
# Ratio of 0 gives black, 100 gives starting color, 50 gives faded halfway to black
def fade(c: tuple, ratio: int):
    return blend(BLACK, c, ratio)


# Add two colors together, constraining sum to 255
def add(c1: tuple, c2: tuple):
    if len(c1) != 3 or len(c2) != 3:
        return GRAY

    return (_constrain(c1[0] + c2[0], 0, 255),
            _constrain(c1[1] + c2[1], 0, 255),
            _constrain(c1[2] + c2[2], 0, 255))


# Constrain the value n to be in the range from min_val to max_val
def _constrain(n: int, min_val: int, max_val: int):
    return max(min(max_val, n), min_val)
