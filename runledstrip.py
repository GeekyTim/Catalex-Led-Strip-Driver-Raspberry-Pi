#!/usr/bin/python
import ledstrip
import time

CLK = 11
DAT = 12

strip = LEDStrip(CLK, DAT)

print("All 0")
strip.setcolor(0, 0, 0)
# time.sleep(1)
print("All 255")
strip.setcolor(255, 255, 255)
time.sleep(.2)
print("Red 255")
strip.setcolor(255, 0, 0)
time.sleep(.2)
print("Green 255")
strip.setcolor(0, 255, 0)
time.sleep(.2)
print("Blue 255")
strip.setcolor(0, 0, 255)
time.sleep(.2)
print("All 0")
strip.setcolor(0, 0, 0)
time.sleep(.2)

for z in range(10):
    for x in range(255):
        # print("X:%d" % (x)
        # y=x*10
        strip.setcolor(x, x, x)
    for x in range(255):
        strip.setcolor(255 - x, 255 - x, 255 - x)

for x in range(20):
    strip.setcolor(255, 0, 0)
    time.sleep(0.1)
    strip.setcolor(0, 0, 255)
    time.sleep(0.1)

print("All 0")
strip.setcolor(0, 0, 0)
# time.sleep(1)
print("Cleanup")
strip.cleanup()
