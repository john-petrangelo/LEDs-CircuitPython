from colors import BLACK, RED, BLUE, GREEN
from models import Add, Gradient, Solid


def make_demo3():
    red_gradient = Gradient("grad_red", BLACK, RED)
    blue_gradient = Gradient("grad_red", BLUE, BLACK)
    green_solid = Solid("green solid", GREEN)

    return Add("Add", [red_gradient, blue_gradient, green_solid])
