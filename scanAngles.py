from pymycobot.mycobot import MyCobot
import time
coord_list = {}
mc = MyCobot('/dev/ttyAMA0',1000000)
for i in range(0,5):
    mc.release_all_servos()
    print("scanning angles, change position within 5 seconds",i)
    time.sleep(5)
    mc.jog_stop()
    coord_list[i] = mc.get_angles()

print(coord_list)

for k,v in coord_list.items():
    print("changing cords, stay near robot and be alert")
    time.sleep(5)
    mc.send_angles(v,30)

mc.release_all_servos()

# dict ={
#     1: [3213.3,3213,123,123],
#     2 :[3214123123,3214,123]
# }

# for k,v in dict.items():
#     print(k,v)
