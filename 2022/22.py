from sys import stdin
import re
from aocd import submit, get_data, lines
from PIL import Image

ll = stdin.read().split('\n\n')
#ll = get_data(day=22).split('\n\n')

grid = [list(x) for x in ll[0].split('\n')]
path = re.findall('\d+|R|L',ll[1])
m = max([len(row) for row in grid])
for y, row in enumerate(grid):
    if len(row) < m:
        grid[y] += [' 'for _ in range(m-len(row))]

d = [(1,0),(0,1),(-1,0),(0,-1),]
di = 0

warps = {}
for i in range(50):
    warps[((100+i,0), (0,-1))] = ((0+i,199),(0,-1),(75, 0, 130))
    warps[((0+i,199), (0,1))] = ((100+i,0),(0,1),(75, 0, 130))

    warps[((50+i,0), (0,-1))] = ((0,150+i),(1,0),(139, 69, 0))
    warps[((0,150+i), (-1,0))] = ((50+i,0),(0,1),(139, 69, 0))

    warps[((149,0+i), (1,0))] = ((99,149-i),(-1,0),(85, 107, 47))
    warps[((99,149-i), (1,0))] = ((149,0+i),(-1,0),(85, 107, 47))

    warps[((50,0+i), (-1,0))] = ((0,149-i),(1,0),(0, 69, 139))
    warps[((0,149-i), (-1,0))] = ((50,0+i),(1,0),(0, 69, 139))

    warps[((50,50+i), (-1,0))] = ((0+i,100),(0,1),(128, 0, 0))
    warps[((0+i,100), (0,-1))] = ((50,50+i),(1,0),(128, 0, 0))

    warps[((50+i,149), (0,1))] = ((49,150+i),(-1,0),(0, 0, 128))
    warps[((49,150+i), (1,0))] = ((50+i,149),(0,-1),(0, 0, 128))

    warps[((100+i,49), (0,1))] = ((99,50+i),(-1,0),(47, 79, 79))
    warps[((99,50+i), (1,0))] = ((100+i,49),(0,-1),(47, 79, 79))


y = 0
for x, g in enumerate(grid[y]):
    if g == '.':
        break

#print(warps.values())
#print(grid)
#print(path)
print(x, y)
pp = []
dii=-1
ppp = set()
def draw():
    global dii,x,y
    #if dii > 400: return
    dii += 1
    if dii%10 > 0: return
    image = Image.new('RGB', (152,202))
    for dy,row in enumerate(grid):
        for dx,c in enumerate(row):
            image.putpixel((dx+1,dy+1), {' ':0,'.': (24, 5, 3),'#': (48, 10, 6)}[c])
    for ii, (dx,dy) in enumerate(ppp):
        image.putpixel((dx+1,dy+1), (0,0,0))
    for ii, (dx,dy) in enumerate(pp):
        image.putpixel((dx+1,dy+1), (255-len(pp)+ii,255-len(pp)+ii,255-len(pp)+ii))
    for (dx,dy),dd in warps:
        image.putpixel((dx+dd[0]+1,dy+dd[1]+1), warps[(dx,dy),dd][2])
#        image.putpixel((dx,dy), {(1,0):(0,50,0),(0,1):(0,100,0),(-1,0):(0,150,0),(0,-1):(0,200,0)}[dd])
    image.putpixel((x+1,y+1), (255,255,255))
    image = image.resize((150*6,200*6), Image.Resampling.NEAREST)
    image.save("frames/22_"+str(dii//10)+".png")

def move(n, d):
    global x,y,di
    for _ in range(n):
        tx,ty = x,y
        while True:
            if ((tx,ty),d) in warps:
                #print((tx,ty), d)
                (tx,ty),dd,_ = warps[((tx,ty),d)]
                if grid[ty][tx] == '#':
                    #print((tx,ty), d, dd)
                    break
                if grid[ty][tx] == '.':
                    di = [(1,0),(0,1),(-1,0),(0,-1),].index(dd)
                    d = dd
            else:
                tx = tx+d[0]
                ty = ty+d[1]
            #if ty == -1: ty = len(grid)-1
            #if tx == -1: tx = len(grid[ty])-1
            #if ty == len(grid): ty = 0
            #if tx == len(grid[ty]): tx = 0
            if grid[ty][tx] == ' ':
                print(' ',tx,ty)
                exit()
                #continue
            if grid[ty][tx] == '#':
                break
            if grid[ty][tx] == '.':
                pp.append((x,y))
                x,y = tx,ty
                draw()
                if len(pp) > 255: ppp.add(pp.pop(0))
                break
#            print(tx,ty)
            break
    #draw()
#    print(n, d)

for p in path:
#    print(p, di)
    if p == 'R':
        di += 1
    elif p == 'L':
        di -= 1
    else:
        p = int(p)
        move(p, d[di%len(d)])
#        print(x,y)

#draw()
print(1000*(y+1) + 4*(x+1) + di%4)
#print(pp)

#for y,row in enumerate(grid):
#    for x,c in enumerate(row):
#        print(pp[(x,y)] if (x,y) in pp else c, end='')
#    print()
print(len(path))
