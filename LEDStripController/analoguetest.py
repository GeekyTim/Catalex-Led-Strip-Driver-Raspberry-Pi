#!/usr/bin/python3
from gpiozero import MCP3008
import time
import urllib3

# The LED Strip server
LEDStripServer = '192.168.13.181'
LEDStripPort = '5000'
LEDStripColourURL = "http://%s:%s/colour" % (LEDStripServer, LEDStripPort)

http = urllib3.PoolManager()

red = MCP3008(channel=0, device=0)
green = MCP3008(channel=1, device=0)
blue = MCP3008(channel=2, device=0)

while True:
    r = int(red.value * 255)
    g = int(green.value * 255)
    b = int(blue.value * 255)

    print('Red: ', r)
    print('Green: ', g)
    print('Blue: ', b)
    req = http.request('GET', LEDStripColourURL, fields = {'r': r, 'g': g, 'b': b})

    time.sleep(1)
