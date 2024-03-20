from pymycobot.mycobot import MyCobot
import time
coord_list = {}
mc = MyCobot('/dev/ttyAMA0',1000000)
print("setting join 1 encorder to 2048")
time.sleep(3)
mc.set_encoder(1, 2048)
print("setting gripper value")

time.sleep(2,)
print("opeing gripper")
mc.set_gripper_state(0, 70)
time.sleep(3)
# Set the state of the gripper so that it quickly closes thegripper at a speed of 70
mc.set_gripper_state(1, 70)
time.sleep(3)
mc.release_all_servos()
time.sleep(3)
mc.set_gripper_value(2048, 70)
