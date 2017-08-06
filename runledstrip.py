#!/usr/bin/python
from ledstrip import LEDStrip
import time

CLK = 17
DAT = 18

strip = LEDStrip(CLK, DAT)

print("All 0")
strip.setcolouroff()
# time.sleep(1)
# print("All 255")
# strip.setcolourwhite()
# time.sleep(1)
# print("Red 255")
# strip.setcolourred()
# time.sleep(1)
# print("Green 255")
# strip.setcolourgreen()
# time.sleep(1)
# print("Blue 255")
# strip.setcolourblue()
# time.sleep(1)
print("FFFFFF")
strip.setcolourhex("FFFFFF")
time.sleep(1)
print("XADA55")
strip.setcolourhex("XADA55")
time.sleep(1)
#
# for x in range(255):
#     strip.setcolourRGB(x, x, x)
# for x in range(255):
#     strip.setcolourRGB(255 - x, 255 - x, 255 - x)
#
# for x in range(20):
#     strip.setcolourRGB(255, 0, 0)
#     time.sleep(0.1)
#     strip.setcolourRGB(0, 0, 255)
#     time.sleep(0.1)


# time.sleep(1)
print("Cleanup")
strip.cleanup()
