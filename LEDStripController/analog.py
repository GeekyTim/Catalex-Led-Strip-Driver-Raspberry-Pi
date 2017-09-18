#!/usr/bin/python3
from time import sleep

from gpiozero import MCP3008

vref = 255
redpot = MCP3008(channel=0)
greenpot = MCP3008(channel=1)
bluepot = MCP3008(channel=2)

while True:
    red = int(redpot.value * vref)
    green = int(greenpot.value * vref)
    blue = int(bluepot.value * vref)
    print(red, green, blue)
    sleep(0.1)
