import colors
import time




def run(pixels):
    while True:
        for pos in range(len(pixels)):
            pixels.fill(colors.BLACK)
            pixels[pos] = colors.YELLOW
            pixels.show()
            time.sleep(0.010)
