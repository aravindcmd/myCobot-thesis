from pymycobot.mycobot import MyCobot
import time
coord_list = []
mc = MyCobot('/dev/ttyAMA0',1000000)
for i in range(0,5):
    mc.release_all_servos()
    print("scanning cord in 5 seconds", )
    time.sleep(5)
    mc.jog_stop()
    coord_list.append(mc.get_coords())

print(coord_list)

for i in coord_list:
    print("changing cord in 3 seconds")
    time.sleep(3)
    mc.send_coords(coord_list[i],20,1)

mc.release_all_servos()
