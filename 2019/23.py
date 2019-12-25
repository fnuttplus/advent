from vm import Computer
from threading import Thread
from queue import Queue
from time import sleep

ins = input()
comps = [Computer(ins, False) for _ in range(50)]

natx,naty = -1,-1
def listen(i):
    global natx, naty
    #print("LISTEN", i)
    while True:
        q = comps[i].outq.get()
        x = comps[i].outq.get()
        y = comps[i].outq.get()
        #print(i, q, x, y)
        if q == 255:
            natx = x
            naty = y
        else:
            comps[q].inq.put(x)
            comps[q].inq.put(y)

for i in range(50):
    #print("START", i)
    comps[i].inq.put(i)
    comps[i].start()
    comps[i].inq.put(-1)

for i in range(50):
    Thread(target=listen, args=(i,)).start()

naty0 = -1
while True:
    sleep(.1)
    for i in range(50):
        if not comps[i].inq.empty():
            #print("NOT IDLE", i)
            break
    else:
        #print("NAT", naty)
        if naty == naty0:
            print(naty)
            break
        naty0 = naty
        comps[0].inq.put(natx)
        comps[0].inq.put(naty)
