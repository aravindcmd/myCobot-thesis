from pymycobot.mycobot import MyCobot
import time
pick_coord_list = {}
mc = MyCobot('/dev/ttyAMA0',1000000)
for i in range(1,6):
    mc.release_all_servos()
    if(i==1):
        print("hover above the pickup location, within 5 seconds")
    elif(i==2):
        print("get the open gripper in range on picking up, within 5 seconds")
    elif(i==3):
        print("now hover back above the location, within 5 seconds")
    elif(i==4):
        print("now hover above the drop location, within 5 seconds")
    else:
        print("now go above get the gripper to the drop point, within 5 seconds")
    time.sleep(5)
    mc.jog_stop()
    pick_coord_list[i] = mc.get_coords()
    

print(pick_coord_list)

for k,v in pick_coord_list.items():
    if(i==1):
        print("hovering above the pickup point, stay alert")
    elif(i==2):
        print("gripper going near")
        time.sleep(2)
        mc.set_gripper_state(1, 70)
    elif(i==3):
        print("hovering above")
    elif(i==4):
        print("going to drop location")
    else:
        print("print dropping off")
        mc.set_gripper_state(0, 70)
    time.sleep(5)
    if(i==1):
        mc.set_gripper_state(0, 70)
    mc.send_coords(v,40,1)

mc.release_all_servos()
mc.set_gripper_state(0, 70)

# dict ={
#     1: [3213.3,3213,123,123],
#     2 :[3214123123,3214,123]
# }

# for k,v in dict.items():
#     print(k,v)
