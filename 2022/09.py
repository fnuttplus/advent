from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

s = get_data(day=9).splitlines()
#s = stdin.read().splitlines()

r = [[0,0] for _ in range(10)]
hx,hy = 0,0
tx,ty = 0,0
ss = set()
d = {'R': (1,0), 'L': (-1,0), 'D': (0,1), 'U': (0,-1),}
j = 0
for line in s:
    j += 1
    a,b = line.split(' ')
    b = int(b)
    dx,dy = d[a]
    for _ in range(b):
        r[0][0] += dx
        r[0][1] += dy
        for i in range(1, len(r)):
            if r[i-1][0] != r[i][0] and r[i-1][1] != r[i][1] and abs(r[i-1][0]-r[i][0])+abs(r[i-1][1]-r[i][1])>2:
                if abs(r[i-1][0]-r[i][0]) == 1:
                    r[i][0] = r[i-1][0]
                if abs(r[i-1][1]-r[i][1]) == 1:
                    r[i][1] = r[i-1][1]
            if r[i-1][0]-r[i][0] == 2: r[i][0] += 1
            if r[i-1][0]-r[i][0] == -2: r[i][0] -= 1
            if r[i-1][1]-r[i][1] == 2: r[i][1] += 1
            if r[i-1][1]-r[i][1] == -2: r[i][1] -= 1

        ss.add(tuple(r[-1]))
    #image = Image.new('L', (308, 302))
    #for x,y in r: image.putpixel((x+57,y+128),250)
    #for x,y in ss: image.putpixel((x+57,y+128),120)
    #image = image.resize((308*4,302*4), Image.Resampling.NEAREST)
    #image.save("frames/09_"+str(j)+".png")

print(len(ss))

#for y in range(-50,50):
#    for x in range(-50,50):
#        print('#' if (x,y) in ss else '.', end="")
#    print()

#print(max([s[0] for s in ss]))
#print(min([s[0] for s in ss]))
#print(max([s[1] for s in ss]))
#print(min([s[1] for s in ss]))
