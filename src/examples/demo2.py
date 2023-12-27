from animations import Rotate, Pulsate
from colors import RED, BLUE
from models import Gradient, Reverse, Map, Window


def make_demo2():
    gradient = Gradient("grad", BLUE, RED)
    rot_grad = Rotate("Rotate Gradient", 2000, gradient)
    rev_grad = Reverse("reverse", rot_grad)

    map_left = Map("map left", 0.0, 1.0, 0.0, 0.5, rot_grad)
    map_right = Map("map right", 0.0, 1.0, 0.5, 1.0, rev_grad)

    window = Window("window", 0.0, 0.5, map_left, map_right)
    pulsation = Pulsate("pulsate", 0.2, 1.0, 2500, 2500, window)

    return pulsation

