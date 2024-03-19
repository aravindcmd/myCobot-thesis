from pymycobot.mycobot import MyCobot
from pymycobot import PI_BAUD, PI_PORT
import RPi.GPIO as GPIO
import numpy as np
import time
import cv2

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

vs = cv2.VideoCapture(0)
print("Camera On: {}".format(vs.isOpened()))
lR = np.array([142, 114, 181])
uR = np.array([194, 255, 255])
lG = np.array([54, 82, 228])
uG = np.array([81, 255, 255])
lB = np.array([83, 228, 206])
uB = np.array([106, 255, 255])

def pump(state):
    if state == 1: #On
        print('Pump on')
        GPIO.output(20, 0)
        GPIO.output(21, 0)
    elif state == 0: #Off
        print('Pump off')
        GPIO.output(20, 1)
        GPIO.output(21, 1)

# def gripper(state):
#     if state == 1: #On
#         print('Pump on')
#         GPIO.output(20, 0)
#         GPIO.output(21, 0)
#     elif state == 0: #Off
#         print('Pump off')
#         GPIO.output(20, 1)
#         GPIO.output(21, 1)

def findContour(mask):
    minArea = 10000
    found = False
    x, y, w, h = 0, 0, 0, 0
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area &gt;= minArea:
            x, y, w, h = cv2.boundingRect(contour)
            found = True
            break
    return x, y, w, h, found

standy = [7.82, -15.82, -110.12, 37.7, -19.59, -123.04]


pickup = [
    [33.92, -5.53, -117.94, 39.63, -21.79, -133.5],
    [32.69, -17.57, -121.46, 52.73, -20.83, -123.31]
]

hover_after_pick_up = [29.0, -4.21, -78.75, -1.75, -23.2, -150.46]

drop_off_point = [-79.27, -16.25, -85.95, 16.78, -15.11, -139.83]


hover_after_drop = [-75.93, -17.49, -57.04, -9.58, -21.0, -136.93]


mc = MyCobot("/dev/ttyAMA0", 1000000)
pump(0)
time.sleep(1)
while True:
    try:
        mc.set_color(255, 255, 255)
	    print("Standy ANGLE ACTIVATED)
        # init the standy angle
        mc.send_angles(standy, 40)
        time.sleep(2)

        dR, dG, dB = False, False, False
        while True:
            # Clearing buffer
            for i in range(30):
                _, frame = vs.read()

            _, frame = vs.read()
            #cv2.imwrite("a.jpg", frame)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            maskR = cv2.inRange(hsv, lR, uR)

            xr, yr, wr, hr, dR = findContour(maskR)

            if dR:
                mc.set_color(255, 0, 0)
                print("Detected Red Block")
                cv2.rectangle(frame, (xr, yr), (xr+wr, yr+hr), (0, 0, 0), 2)



            cv2.imshow("frame", frame)
            cv2.waitKey(1)
            if dR:
                break

        for angle in pickup:
            mc.send_angles(angle, 40)
            time.sleep(1.5)
        #pickup
        pump(1)
        time.sleep(1)
        mc.send_angles(hover_after_pick_up, 40)
        time.sleep(1)
        mc.send_angles(drop_off_point, 40)
        time.sleep(3)
        pump(0)
        time.sleep(3.5)
        mc.send_angles(hover_after_drop, 40)
        time.sleep(1.5)

    except KeyboardInterrupt:
        break
pump(0)
time.sleep(1)
mc.send_angles(pickup[1], 40)
time.sleep(3)
mc.release_all_servos()
GPIO.cleanup()
vs.release()
cv2.destroyAllWindows()
time.sleep(1)
