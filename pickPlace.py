from pymycobot.mycobot import MyCobot
import time
coord_list = {}
mc = MyCobot('/dev/ttyAMA0',1000000)
flag = "n"
for i in range(0,6):
    mc.release_all_servos()
    print("scanning angles, change position within 5 seconds")
    if(i==0):
        print("set the standby postion")
    elif(i ==1):
        print("set the hover above target postion")
    elif(i ==2):
        print("set the gripper within target reach")
    elif(i == 3):
        print("set the hover above drop postion")
    elif(i == 4):
        print("set the gripper within the drop reach")
    else:
        print("set the exit safe postion")
    flag = input("enter y once done setting")
    # time.sleep(5)
    mc.jog_stop()
    coord_list[i] = mc.get_angles()

print(coord_list)

mc.set_gripper_state(0, 70)
for k,v in coord_list.items():
    print("changing angles, stay near robot and be alert")
    if(k == 2):
        mc.set_gripper_state(1,70)
    if(k == 4):
        mc.set_gripper_state(0,70)
    time.sleep(5)
    mc.send_angles(v,30)

mc.release_all_servos()

# dict ={
#     1: [3213.3,3213,123,123],
#     2 :[3214123123,3214,123]
# }

# for k,v in dict.items():
#     print(k,v)
