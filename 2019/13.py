from vm import Computer

comp = Computer(input(), False)
comp.ins[0] = 2
comp.start()

c = {}
paddle = None
score = 0
while True:
    q0 = comp.outq.get()
    if q0 == None: break
    q1 = comp.outq.get()
    q2 = comp.outq.get()
    if q0 == -1 and q1 == 0:
        score = q2
        if False:
            print(q2)
            for y in range(min([p[1] for p in c]),max([p[1] for p in c])+1):
                for x in range(min([p[0] for p in c]),max([p[0] for p in c])+1):
                    print(c[(x,y)],end="")
                print()
    else:
        if q2 == 0:  c[(q0,q1)] = " "
        if q2 == 1:  c[(q0,q1)] = "#"
        if q2 == 2:  c[(q0,q1)] = "="
        if q2 == 3: 
            c[(q0,q1)] = "_"
            paddle = [q0,q1]
        if q2 == 4:
            c[(q0,q1)] = "o"
            ball = (q0,q1)
            if paddle:
                if paddle[0] > ball[0]:
                    comp.inq.put(-1)
                    paddle[0] -= 1
                elif paddle[0] < ball[0]:
                    comp.inq.put(1)
                    paddle[0] += 1
                else:
                    comp.inq.put(0)
            else:
                comp.inq.put(0)

print(score)
