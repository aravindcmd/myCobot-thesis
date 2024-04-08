from pymycobot.mycobot import MyCobot
from pymycobot import PI_BAUD, PI_PORT
import numpy as np
import time
import cv2


vs = cv2.VideoCapture(0)
print("Camera On: {}".format(vs.isOpened()))
lR = np.array([142, 114, 181])
uR = np.array([194, 255, 255])
lG = np.array([54, 82, 228])
uG = np.array([81, 255, 255])
lB = np.array([83, 228, 206])
uB = np.array([106, 255, 255])

def gripperControl(state):
    if state == 1: #On
        mc.set_gripper_state(1,70)
        time.sleep(2)
    elif state == 0: #Off
        print("Gripper opening")
        mc.set_gripper_state(0,70)
        time.sleep(2)

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

camera = coord_list.get(0)
hover_pickup = coord_list.get(1)
hover_angle = coord_list[3]
drop_angle = coord_list[4]
comeback_angle = camera

# pickup = [
    
#     # [33.92, -5.53, -117.94, 39.63, -21.79, -133.5],
#     # [32.69, -17.57, -121.46, 52.73, -20.83, -123.31]
# ]

pickup_red = color_list.get("red")
pickup_green = color_list.get("green")
pickup_blue = color_list.get("blue")

# comebackR = [-75.93, -17.49, -57.04, -9.58, -21.0, -136.93]
# comebackB = [-51.85, -17.22, -60.29, -0.26, -20.3, -136.93]
# comebackG = [-35.77, -31.02, -41.3, -3.69, -19.95, -164.44]

mc = MyCobot("/dev/ttyAMA0", 1000000)
pump(0)
time.sleep(1)
while True:
    try:
        mc.set_color(255, 255, 255)
	    print("CAMERA ANGLE ACTIVATED)
        # init the camera angle
        mc.send_angles(camera, 40)
        time.sleep(2)

        red_detected, green_detected, blue_detected = False, False, False
        while True:
            # Clearing buffer
            for i in range(30):
                _, frame = vs.read()

            _, frame = vs.read()
            #cv2.imwrite("a.jpg", frame)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            maskR = cv2.inRange(hsv, lR, uR)
            maskG = cv2.inRange(hsv, lG, uG)
            maskB = cv2.inRange(hsv, lB, uB)

            xr, yr, wr, hr, red_detected = findContour(maskR)
            xg, yg, wg, hg, green_detected = findContour(maskG)
            xb, yb, wb, hb, blue_detected = findContour(maskB)

            if red_detected:
                pickup_angle = pickup_red
                mc.set_color(255, 0, 0)
                print("Detected Red Block")
                cv2.rectangle(frame, (xr, yr), (xr+wr, yr+hr), (0, 0, 0), 2)
            elif green_detected:
                pickup_angle = pickup_green
                mc.set_color(0, 255, 0)
                print("Detected Green Block")
                cv2.rectangle(frame, (xg, yg), (xg+wg, yg+hg), (0, 0, 0), 2)
            elif blue_detected:
                pickup_angle = pickup_blue
                mc.set_color(0, 0, 255)
                print("Detected Blue Block")
                cv2.rectangle(frame, (xb, yb), (xb+wb, yb+hb), (0, 0, 0), 2)



            cv2.imshow("frame", frame)
            cv2.waitKey(1)
            if red_detected or green_detected or blue_detected:
                break

        gripper_control(0)
        time.sleep(4)
        mc.send_angles(hover_pickup, 40)
        time.sleep(4)
        mc.send_angles(pickup_angle, 40)
        time.sleep(1)
        mc.send_angles(hover_angle, 40)
        time.sleep(3)
        mc.seng_angles(drop_angle,40)
        pump(0)
        time.sleep(3.5)
        mc.send_angles(comeback_angle, 40)
        time.sleep(1.5)

    except KeyboardInterrupt:
        break
pump(0)
time.sleep(1)
mc.send_angles(pickup[1], 40)
time.sleep(3)
mc.release_all_servos()
vs.release()
cv2.destroyAllWindows()
time.sleep(1)
