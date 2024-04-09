from pymycobot.mycobot import MyCobot
from pymycobot import PI_BAUD, PI_PORT
import RPi.GPIO as GPIO
import time
import cv2

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

def pump(state):
    if state == 1: #On
        print('Pump on')
        GPIO.output(20, 0)
        GPIO.output(21, 0)
    elif state == 0: #Off
        print('Pump off')
        GPIO.output(20, 1)
        GPIO.output(21, 1)


pump(0)
time.sleep(1)
# mc.send_angles(pickup[1], 40)
pumpt(1)
time.sleep(3)
pump(0)
mc.release_all_servos()
GPIO.cleanup()
# vs.release()
# cv2.destroyAllWindows()
time.sleep(1)
