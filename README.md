# Open-Smart RGB LED Strip Driver for the Raspberry Pi
This code was forked from https://github.com/schlank/Catalex-Led-Strip-Driver-Raspberry-Pi

This code is used to control RGB strips using the Open-Smart Arduino controller that I obtained from DealExtreme: http://www.dx.com/p/full-color-rgb-led-strip-driver-module-for-arduino-blue-black-314667

## LEDStrip Class

### Pin Connections

Connect your Raspberry Pi to the input of the controller board.

Choose any two GPIO Pins; one to provide the Clock signal (CLK), the other the Data (DAT).

|Pi|Open-Smart Controller|
|--|---------------------|
|Gnd|Gnd|
|+5v|Vcc|
|DAT|Din|
|CLK|Cin|

Place ledstrip.py into the same directory as your code.

In your code, import the file:

    from ledstrip import LEDStrip

Create a new LED Strip which uses your chosen pins (CLK and DAT) with, e.g.:

    CLK = 17
    DAT = 18
    strip = LEDStrip(CLK, DAT)

Set the colour of the LED strip with

    strip.setcolorrgb(red, green, blue):

The following methods are public:

    setcolourrgb(r, g, b) - Sets the LED strip to colour rgb where r, g, b are in the range 0 to 255
    setcolourwhite() - Sets the strip to white
    setcolourred() - Sets the strip to Red
    setcolourgreen() - Sets the strip to Green
    setcolourblue() - Sets the strip to Blue
    setcolouroff() - Turns the strip off
    setcolourhex('hex') - Sets the LED strip to the hex colour 'hex' in range '000000' to 'FFFFFF'
