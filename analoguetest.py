#!/usr/bin/python3
from gpiozero import MCP3008
import time
import urllib3

# The LED Strip server
LEDStripServer = '192.168.13.181'
LEDStripPort = '5000'
LEDStripColourURL = "http://%s:%s/colour" % (LEDStripServer, LEDStripPort)

http = urllib3.PoolManager()

adc = MCP3008(channel=0, device=0)

while True:
    red = int(adc.value * 255)

    r = http.request('GET', LEDStripColourURL, fields = {'r': red, 'g': red, 'b': red})

    time.sleep(0.1)
