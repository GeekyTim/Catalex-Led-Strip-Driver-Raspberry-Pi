from gpiozero import Button
from time import sleep
vref = 3.3
#adc = MCP3008(channel=0)

whitebutton = Button(4)
redbutton = Button(17)
greenbutton = Button(18)
bluebutton = Button(27)

bluebutton.wait_for_press()
print("Button Pressed")

