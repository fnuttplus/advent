from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

ll = stdin.read().splitlines()
ll = get_data(day=14).splitlines()

walls = set()
m = 0
for l in ll:
    p = l.split(' -> ')
    x1,y1 = map(int, p[0].split(','))
    for i in range(1, len(p)):
        print(p[i])
        x2,y2 = map(int, p[i].split(','))
        a = 1 if x2 > x1 else -1
        b = 1 if y2 > y1 else -1
        for x in range(x1,x2+a,a):
            for y in range(y1,y2+b,b):
                walls.add((x,y))
                if y > m:
                    m = y
        x1=x2
        y1=y2

    print(walls)

t = (500,0)
s = (t[0], t[1])
print(m)

minx = min([w[0] for w in walls])
maxx = max([w[0] for w in walls])

sand = set()
i = 0
path = set()
def draw(i):
    image = Image.new('RGB', ((maxx-minx)+1, m+1))
    for w in walls: image.putpixel((w[0] - minx, w[1]), (68,31,32))
    for w in sand: image.putpixel((w[0] - minx, w[1]), (209,146,83))
    for w in path: image.putpixel((w[0] - minx, w[1]), (188,92,71))
    image.putpixel((500 - minx, 0), (207,82,26))
    image = image.resize((((maxx-minx)+2)*6,(m+1)*6), Image.Resampling.NEAREST)
    #image.putpixel((500,0), 100)
    image.save("frames/14_"+str(i)+".png")

while True:
    #print(s)
    if not ((s[0],s[1]+1) in (walls|sand) or s[1]+1 == m + 2):
        s = (s[0],s[1]+1)
        if s[1] > m:
            draw(i+1)
            break
        path.add(s)
        continue

    if not ((s[0]-1,s[1]+1) in (walls|sand) or s[1]+1 == m + 2):
        s = (s[0]-1,s[1]+1)
        path.add(s)
        continue

    if not ((s[0]+1,s[1]+1) in (walls|sand) or s[1]+1 == m + 2):
        s = (s[0]+1,s[1]+1)
        path.add(s)
        continue


    if s == t:
        i += 1
        break
    #walls.add(s)
    sand.add(s)
    i += 1
    s = (t[0], t[1])

    draw(i)
    path = set()

for y in range(200):
    for x in range(450,550):
        print('#' if (x,y) in walls else '.',end='')
    print()
print(i)
