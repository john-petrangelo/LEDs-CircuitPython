from animations import Rotate
from colors import BLUE, GREEN, RED, YELLOW
from models import Gradient, Map, Window


def make_demo1():
    grad_left = Gradient("grad-right", BLUE, GREEN)
    grad_right = Gradient("grad-left", RED, YELLOW)

    rot_left = Rotate("rotate down", -3000, grad_left)
    rot_right = Rotate("rotate up", 1000, grad_right)

    # pulsation = Pulsate("pulsate", 0.2, 1.0, 2500, 2500, rot_left)

    map_left = Map("map left", 0.0, 1.0, 0.0, 0.3, rot_left)
    map_right = Map("map right", 0.0, 1.0, 0.3, 1.0, rot_right)

    window = Window("window", 0.0, 0.3, map_left, map_right)
    rot_window = Rotate("rotate window", -10000, window)

    return rot_window
