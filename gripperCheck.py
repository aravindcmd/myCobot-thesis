coord_list = {}
mc = MyCobot('/dev/ttyAMA0',1000000)
flag = "n"
setPose = input('do you want to lock this pose')
mc.jog_stop()
time.sleep(2)
mc.set_gripper_state(0, 70)
time.sleep(2)
mc.set_gripper_state(1,70)
mc.jog_stop()
