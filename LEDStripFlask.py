#!/usr/bin/python

from flask import Flask, request
from ledstrip import LEDStrip
import time

CLK = 17
DAT = 18

strip = LEDStrip(CLK, DAT)
app = Flask(__name__)

strip.setcolourred()
time.sleep(0.2)
strip.setcolourgreen()
time.sleep(0.2)
strip.setcolourblue()
time.sleep(0.2)
strip.setcolouroff()

@app.route("/")
def hello():
    strip.setcolouroff()
    return "Hello World!"

@app.route("/red")
def redled():
    strip.setcolourred()
    return "red"

@app.route("/green")
def greenled():
    strip.setcolourgreen()
    return "green"

@app.route("/blue")
def blueled():
    strip.setcolourblue()
    return "blue"


@app.route("/white")
def whiteled():
    strip.setcolourwhite()
    return "white"


@app.route("/off")
def offled():
    strip.setcolouroff()
    return "off"

@app.route("/colour")
def colourled():
    red = request.args.get('r', '')
    green = request.args.get('g', '')
    blue = request.args.get('b', '')
    print(int(red), int(green), int(blue))
    strip.setcolourrgb(int(red), int(green), int(blue))
    return "colour"

