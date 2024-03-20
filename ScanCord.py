from pymycobot.mycobot import MyCobot

res = []
mc = MyCobot('/dev/ttyAMA0',1000000)
for i in range(0,5):
    mc.release_all_Servos()
    print("scanning cord in 5 seconds", )
    time.sleep(5)
    mc.jog_stop()
    res.append(mc.get_coords())

print(res)
    
    
