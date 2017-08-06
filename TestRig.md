# Test Rig

![alt text](https://github.com/GeekyTim/Open-Smart-RGB-LED-Strip-Driver-for-Raspberry-Pi/blob/master/images/RGBLED_Test_rig.jpg "RGB LED Test Rig")

## Parts List

+ Raspberry Pi Zero W with Raspbian Lite on SD
+ Open-Smart RGB LED Controller (http://www.dx.com/p/full-color-rgb-led-strip-driver-module-for-arduino-blue-black-314667 or http://www.dx.com/p/full-color-rgb-led-strip-driver-module-w-dc-jack-for-arduino-440804)
+ Mini DC adjustable step down module
+ 12v RGB LED Strip
+ Short Micro USB Cable
+ USB A Socket
+ Barrel Jack Sockets
+ 12v power supply
+ 4 M-M Jumper wires
+ Various other wires
+ Heat Shrink

## Build

1. Connect the barrel jack to the input of the Mini DC adjustable step down module
2. Connect output of module to the USB A socket (Get + and GND round the right way!)
3. Plug inthe 12v power supply to the jack, and adjust the step down module so that the output is roughly 5.2v. Disconnect for the rest oft he assembly.
4. Take 12v directly from the barrel jack to the input of the RGB LED Controller
5. Connect the RGB LED strip to the controller output
6. To connect your Raspberry Pi to Controller pin connections, choose any two GPIO Pins; one to provide the Clock signal (CLK), the other the Data (DAT). Connect as follows:

|Pi|Open-Smart Controller|
|--|---------------------|
|Gnd|Gnd|
|+5v|Vcc|
|DAT|Din|
|CLK|Cin|

7. Plug the USB A socket to the Raspberry Pi power input with a USB to Micro USB cable.

## Raspbian Lite

Start with the latest version of [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/) written to a microSD card.  Connect it to your wireless network (follow instructions elsewhere on the 'net).

Update to the latest versions of all software with:

    sudo apt-get update
    sudo apt-get upgrade
    
Install python3 and other prerequisits:

    sudo spt-get install python3 python3-rpi.gpio git

## LEDStrip

Clone the Open-Smart RGB LED Strip library from GIT:

    git clone https://github.com/GeekyTim/Open-Smart-RGB-LED-Strip-Driver-for-Raspberry-Pi
    
Test the LEDStrip code by running the test code:

    python3 runledstrip.py
    
Copy the ledstrip.py to the same folder that you develop your own code in.