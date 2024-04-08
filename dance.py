from pymycobot import MyCobot
import time
mc = MyCobot("COM6")
# print(mc.get_angles())
# mc.release_all_servos()
# [-2.54, -140.36, 155.03, -14.94, 0.43, -31.02]
for i in range(1):
    mc.send_angles([3.77, -140.09, 150.11, 35.5, -15.46, -30.93],30)
    time.sleep(2)
    mc.send_angles([9.14, -73.38, 102.91, -26.36, -4.92, -31.02],30)
    time.sleep(2)
    mc.send_angles([-86.04, -73.65, 102.74, -31.11, -4.74, -31.02],30)
    time.sleep(2)
    mc.send_angles([94.21, -73.65, 102.83, -35.06, -2.28, -31.02],30)
    time.sleep(2)
    mc.send_angles([1.4, -79.45, 102.74, -29.79, -2.28, -31.02],30)
    time.sleep(2)
    mc.send_angles([1.14, -10.28, 9.31, 0.7, -1.75, -31.02],30)
    time.sleep(2)
    mc.send_angles([4.21, 98.34, -124.01, 25.22, -6.15, -31.02],30)
    time.sleep(2)
    mc.send_angles([3.69, -99.66, 131.48, -50.97, 4.57, -31.02],30)
    time.sleep(2)
    mc.send_angles([6.5, 0.17, -96.06, 110.3, 1.05, -31.02],30)
    time.sleep(2)


    mc.send_angles([6.41, 0.87, 123.48, -64.42, 0.7, -31.02],30)
    time.sleep(2)
    mc.send_angles([6.5, 0.17, -96.06, 110.3, 1.05, -31.02],30)
    time.sleep(2)
    mc.send_angles([-63.28, -102.04, 99.58, 7.91, 0.08, -31.02],30)
    time.sleep(2)
    mc.send_angles([-62.05, 76.46, -116.19, 38.4, 58.71, -31.02],30)
    time.sleep(2)
    mc.send_angles([3.16, -104.58, 100.1, 5.36, 4.48, -31.02],30)
    time.sleep(2)
    mc.send_angles([94.13, 86.74, 2.37, -84.28, -92.54, -31.02],30)
    time.sleep(2)
    mc.send_angles([0,0,0,0,0,0],30)
    t = 12
    while t>0:
        # 
        mc.set_color(0, 255, 0)
        time.sleep(0.5)
        # 
        mc.set_color(255, 0, 0)
        time.sleep(0.5)   
        #   
        mc.set_color(255, 255, 0)    
        time.sleep(0.5)    
        t-=1.5
    
 
