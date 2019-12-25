from vm import Computer

comp = Computer(input(), False)
comp.ins[0] = 2
comp.start()
for c in """A,B,B,C,B,C,B,C,A,A
L,6,R,8,L,4,R,8,L,12
L,12,R,10,L,4
L,12,L,6,L,4,L,4
N
""": comp.inq.put(ord(c))

x,y = 0,0
c = {}
i = 0
while True:
    q = comp.outq.get()
    if q is None: break
    if q > 255: print(q)
    if q == 10:
        y += 1
        x = 0
    else:
        x += 1
    if chr(q) == "#":
        c[(x,y)] = 1
        if (x-1, y-1) in c and (x, y-1) in c and (x+1, y-1) in c and (x, y-2) in c:
            i += ((x-1)*(y-1))
            print("o", end="")
        else:
            print(chr(q), end="")
    elif chr(q) == "^":
        x0, y0, d = x, y, 1
    else:
        print(chr(q), end="")

x,y = x0,y0
dd = {1:(0,-1),2:(1,0),3:(0,1),4:(-1,0),}
while True:
    if (x+dd[d][0],y+dd[d][1]) in c:
        x += dd[d][0]
        y += dd[d][1]
        i += 1
    else:
        print(i, end=",")
        i = 0
        a = 4 if d==1 else d-1
        b = 1 if d==4 else d+1
        if (x+dd[a][0],y+dd[a][1]) in c:
            print("L", end=",")
            d = a
        elif (x+dd[b][0],y+dd[b][1]) in c:
            print("R", end=",")
            d = b
        else: break
