from pymycobot.mycobot import MyCobot
import time
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
mc = MyCobot('/dev/ttyAMA0',1000000)
time.sleep(5)
mc.send_angles([0,0,0,0,0,0],0)
time.sleep(10)
mc.send_angles([0,0,(-130),0,0,0],0)
time.sleep(10)
mc.send_angles([0,0,(-130),60,0,0],0)
time.sleep(10)
mc.send_angles([0,(-20),(-130),60,0,0],0)
time.sleep(10)
pump(1)
time.sleep(5)
time.sleep(10)
mc.send_angles([0,0,(-90),90,0,0],0)
time.sleep(4)
mc.send_angles([90,0,(-90),90,0,0],30)
time.sleep(10)
mc.send_angles([90,(-20),(-60),(-10),0,0],30)
pump(0)
time.sleep(10)
mc.send_angles([0,0,0,0,0,0],0)

time.sleep(2)
# mc.send_angles(pickup[1], 40)
#pump(1)
#time.sleep(3)
#pump(0)
#mc.release_all_servos()
GPIO.cleanup()
# vs.release()
# cv2.destroyAllWindows()
#time.sleep(1)





# time.sleep(2)
# mc.send_angles([0,0,0,0,0,0],0)
# time.sleep(10)
# mc.send_angles([0,0,(-130),0,0,0],0)
# time.sleep(10)
# mc.send_angles([0,0,(-130),60,0,0],0)
# time.sleep(10)
# mc.send_angles([0,(-20),(-130),60,0,0],0)
# time.sleep(2)
# pump(1)
# time.sleep(5)
# mc.send_angles([0,0,(-90),90,0,0],0)
# time.sleep(10)
# mc.send_angles([90,0,(-90),90,0,0],0)
# time.sleep(10)
# mc.send_angles([90,0,(-90),(-10),0,0],0)
# time.sleep(5)
# time.sleep(5)
# pump(0)
# mc.send_angles([0,0,0,0,0,0],0)

# time.sleep(2)
# # mc.send_angles(pickup[1], 40)
# #pump(1)
# #time.sleep(3)
# #pump(0)
# #mc.release_all_servos()
# GPIO.cleanup()
# # vs.release()
# # cv2.destroyAllWindows()
# #time.sleep(1)
