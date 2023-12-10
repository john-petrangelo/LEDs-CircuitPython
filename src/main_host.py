import wx
import random

import colors


class CircleDrawingPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, _):
        dc = wx.PaintDC(self)
        self.draw_circles(dc)

    def draw_circles(self, dc):
        for _ in range(10):
            radius = random.randint(10, 50)
            x = random.randint(radius, self.GetSize().width - radius)
            y = random.randint(radius, self.GetSize().height - radius)
            color = wx.Colour(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            dc.SetBrush(wx.Brush(color))
            dc.DrawCircle(x, y, radius)


class CircleDrawingFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.panel = CircleDrawingPanel(self)
        self.SetSize((1024, 320))

        # Set up a timer to change the background color every second
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(10)

        self.Centre()
        self.Show(True)

    def on_timer(self, _):
        # Change the background color of the frame
        self.SetBackgroundColour(wx.Colour(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.Refresh()


if __name__ == "__main__":
    PIXELS_ROWS_COUNT = 8
    PIXELS_COLS_COUNT = 8
    PIXELS_COUNT = PIXELS_ROWS_COUNT * PIXELS_COLS_COUNT
    pixels = [tuple(colors.BLACK) for x in range(PIXELS_COUNT)]
    print(f"There are {len(pixels)} pixels")

    app = wx.App(False)
    frame = CircleDrawingFrame(None, title="Neopixel Animation Simulator")
    app.MainLoop()
