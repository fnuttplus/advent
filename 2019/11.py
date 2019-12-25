from vm import Computer

comp = Computer(input())
comp.start()

d,x,y = 0,0,0
c = {}
comp.inq.put(1)
while True:
    q0 = comp.outq.get()
    if q0 == None: break
    q1 = comp.outq.get()
    c[(x,y)] = q0
    d = (d + (-1 if q1 == 0 else 1))%4
    if d == 0: y-=1
    elif d == 1: x+=1
    elif d == 2: y+=1
    elif d == 3: x-=1
    comp.inq.put(c[(x,y)] if (x,y) in c else 0)

print(len(c))
for y in range(min([p[1] for p in c]),max([p[1] for p in c])+1):
    for x in range(min([p[0] for p in c]),max([p[0] for p in c])):
        print("#" if (x,y) in c and c[(x,y)] == 1 else " ",end="")
    print()
