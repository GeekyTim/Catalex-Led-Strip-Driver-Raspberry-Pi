from gpiozero import LED
from time import sleep
vref = 3.3
#adc = MCP3008(channel=0)

redled = LED(19)
greenled = LED(20)
blueled = LED(21)

whitebuttonled = LED(22)
redbuttonled = LED(23)
greenbuttonled = LED(24)
bluebuttonled = LED(25)


redled.on()
greenled.on()
blueled.on()

whitebuttonled.on()
redbuttonled.on()
greenbuttonled.on()
bluebuttonled.on()

sleep(10)

