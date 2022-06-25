import keypress
import keypress as kp
from djitellopy import tello
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def keyPressed():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50
    if kp.getKey("LEFT"): lr = -speed
    if kp.getKey("RIGHT"): lr = speed
    if kp.getKey("UP"): fb = speed
    if kp.getKey("DOWN"): fb = -speed
    if kp.getKey("w"): ud = speed
    if kp.getKey("s"): ud = -speed
    if kp.getKey("a"): yv = speed
    if kp.getKey("d"): yv = -speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()
    return [lr, fb, ud, yv]
    

while True:
    dirs = keyPressed()
    me.send_rc_control(dirs[0], dirs[1], dirs[2], dirs[3])
    sleep(0.05)