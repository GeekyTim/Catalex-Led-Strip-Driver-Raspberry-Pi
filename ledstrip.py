#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class LEDStrip:

    def __init__(self, clock, data):
        self.__clock = clock
        self.__data = data
        self.__delay = 0
        GPIO.setup(self.__clock, GPIO.OUT)
        GPIO.setup(self.__data, GPIO.OUT)

    @staticmethod
    def cleanup():
        GPIO.cleanup()


    def __sendclock(self):
        GPIO.output(self.__clock, False)
        time.sleep(self.__delay)
        GPIO.output(self.__clock, True)
        time.sleep(self.__delay)


    def __send32zero(self):
        for x in range(32):
            GPIO.output(self.__data, False)
            Clock()

    @staticmethod
    def __getcode(self, dat):
        tmp = 0
        if ((dat & 0x80) == 0):
            tmp |= 0x02
        if ((dat & 0x40) == 0):
            tmp |= 0x01
        return tmp


    def setcolor(self, red, green, blue):
        dx = 0
        dx |= 0x03 << 30
        dx |= self.__getcode(blue)
        dx |= self.__getcode(green)
        dx |= self.__getcode(red)

        dx |= blue << 16
        dx |= green << 8
        dx |= red

        self.__senddata(dx)


    def __senddata(self, dx):
        self.__send32zero()
        for x in range(32):
            if ((dx & 0x80000000) != 0):
                GPIO.output(self.__data, True)
            else:
                GPIO.output(self.__data, False)
            dx <<= 1
            self.__sendclock()
        self.__send32zero()
