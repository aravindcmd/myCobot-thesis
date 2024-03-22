from pymycobot.mycobot import MyCobot
import time
coord_list = {}
mc = MyCobot('/dev/ttyAMA0',1000000)
flag = 0
mc.set_gripper_state(0,70)
time.sleep(3)

mc.release_all_servos()
