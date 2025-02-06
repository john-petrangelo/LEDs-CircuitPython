# Luminaria-Python
Library for animating NeoPixel LEDs with CircuitPython

Tested only on RaspberryPi Pico devices

Development was stopped on this project because the render times using Python were
too slow. It's still a fun playground to expolore lighting effects
running in a window on your host development machine.

# Dependencies
The following must be copied into the `lib` directory on your CircuitPython device:
- adafruit_led_animation/
- adafruit_pixelbuf.mpy
- neopixel.mpy

# Running on Development Host
You can run programs locally on by running the src/other/main_host.py script.

NOTE: You must install the wxPython package for local host graphics support.

    pip install wxPython
