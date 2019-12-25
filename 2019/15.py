from vm import Computer

comp = Computer(input(), False)
comp.mod(0,224,3)
comp.start()

c = {}
x,y = 0,0
i = -1
n = 1
d = 0
dd = ((0,-1,3),(0,1,2),(-1,0,0),(1,0,1))
while n < 44:
    i += 1
    if i == n or i == 2*n:
        d = dd[d][2]
    if i == 2*n:
        n += 1
        i = 0
    x += dd[d][0]
    y += dd[d][1]

    comp.inq.put(d+1)
    q = comp.outq.get()

    if q == 0: c[(x,y)] = "█"
    elif q == 1: c[(x,y)] = " "
    elif q == 2:
        c[(x,y)] = "!"
        print(x,y)

del c[(x,y)]
del c[(x,y-1)]
miny, maxy = min([p[1] for p in c]), max([p[1] for p in c])+1
minx, maxx = min([p[0] for p in c]), max([p[0] for p in c])+1
for y in range(miny,maxy):
    for x in range(minx,maxx):
        try: print(c[(x,y)],end="")
        except: print("?",end="")
    print()

c[(0,0)] = " "
#x,y = 0,0
x,y = 18,18
s = [(x,y,0)]
c[(x,y)] = 0
while s:
    x,y,i = s.pop(0)
    for dx,dy,_ in dd:
        if (x+dx, y+dy) in c:
            if c[(x+dx, y+dy)] == " ":
                s.append((x+dx, y+dy, i+1))
                c[(x+dx, y+dy)] = i+1
            elif c[(x+dx, y+dy)] == "!":
                i += 1
                s = None
print(i)

if False:
    from PIL import Image
    image = Image.new('L', (maxx - minx, maxy - miny))
    cc = {"#": 0, " ": 20, }
    image.putdata([cc[c[(x,y)]] if c[(x,y)] in [" ", "#"] else 256-c[(x,y)]//1.5 for y in range(miny,maxy) for x in range(minx,maxx)])
    image = image.resize((1000,1000), Image.NEAREST)
    image.save("advent15.png")
