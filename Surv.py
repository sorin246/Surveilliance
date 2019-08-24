from flask import Flask
from flask import render_template, request
import RPi.GPIO as G
import time
app = Flask(_name_)
m11=18
m12=23
m21=24
m22=25

G.setwarnings(False)
G.setmode(G.BCM)
G.setup(m11, G.OUT)
G.setup(m12, G.OUT)
G.setup(m21, G.OUT)
G.setup(m22, G.OUT)

G.output(m11, 0)
G.output(m12, 0)
G.output(m21, 0)
G.output(m22, 0)
print("DONE")

a = 1

@app.route("/")
def index():
    return render_template('surv.html')
@app.route('/left_side')
def left_side():
    print("LEFT")
    G.output(m11, 0)
    G.output(m12, 0)
    G.output(m21, 1)
    G.output(m22, 0)
    return "true"

@app.route('/right_side')
def right_side():
    print("RIGHT")
    G.output(m11, 1)
    G.output(m12, 0)
    G.output(m21, 0)
    G.output(m22, 0)
    return "true"

@app.route('/up_side')
def up_side():
    print("FORWARD")
    G.output(m11, 1)
    G.output(m12, 0)
    G.output(m21, 1)
    G.output(m22, 0)
    return "true"

@app.route('/down_side')
def down_side():
    print("BACKWARDS")
    G.output(m11, 0)
    G.output(m12, 1)
    G.output(m21, 0)
    G.output(m22, 1)
    return "true"

@app.route('/stop')
def stop():
    print("stop")
    G.output(m11, 0)
    G.output(m12, 0)
    G.output(m21, 0)
    G.output(m22, 0)
    return "true"

if__name__=="__main__"
print("start")
app.run(host = "0.0.0.0", port = 5010)
