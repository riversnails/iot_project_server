#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bluetooth import *
from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time


app = Flask(__name__)

socket = BluetoothSocket( RFCOMM )
socket.connect(("98:D3:91:FD:F6:EA", 1))

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

@app.route("/")
def helloworld():
    return render_template("index.html")
    
@app.route("/<user>")
def user(user):
    return render_template("helloworld.html", name = user)

@app.route("/spek")
def spek():
    state = request.args.get("state", "error")
    if state == "on":
        socket.send("SPEK_ON")
        return "ok"
    elif state == "off":
        socket.send("SPEK_OFF")
        return "ok"
        
    return "false"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
