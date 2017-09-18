#!/usr/bin/python
import time

from ledstrip import LEDStrip

CLK = 17
DAT = 18

strip = LEDStrip(CLK, DAT)

print("Off")
strip.setcolouroff()
time.sleep(1)

print("White")
strip.setcolourwhite()
time.sleep(1)

print("Red")
strip.setcolourred()
time.sleep(1)

print("Green")
strip.setcolourgreen()
time.sleep(1)

print("Blue")
strip.setcolourblue()
time.sleep(1)

print("RGB 128,128,0")
strip.setcolourrgb(128, 128, 0)
time.sleep(1)

print("Hex BADA55")
strip.setcolourhex("BADA55")
time.sleep(1)

print("Invalid Hex XADA55")
strip.setcolourhex("XADA55")
time.sleep(1)

print("Off")
strip.setcolouroff()
time.sleep(1)

print("Fade in and out")
for x in range(255):
    strip.setcolourrgb(x, x, x)
for x in range(255):
    strip.setcolourrgb(255 - x, 255 - x, 255 - x)

print("Flash red/blue")
for x in range(20):
    strip.setcolourred()
    time.sleep(0.1)
    strip.setcolourblue()
    time.sleep(0.1)

print("Cleanup")
strip.cleanup()
