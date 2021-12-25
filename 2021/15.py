from sys import stdin
#from aocd import lines, submit
from aoc import grid

lines = stdin.read().splitlines()

cr = [[int(x) for x in list(line)] for line in lines]
r = []
for _ in range(len(cr)*5):
    r.append([0]*len(cr[0])*5)
for x in range(5):
    for y in range(5):
        for x1 in range(len(cr[0])):
            for y1 in range(len(cr)):
                r[len(cr) * y + y1][len(cr[0]) * x + x1] = ((cr[y1][x1] + (x+y) -1) % 9) + 1
#print(r)
#print(cr[0])
print(len(r[0]), len(r))

g = grid(r)
c = g.bfs(0,0)

print(c[-1][-1][0])

exit()
from PIL import Image
image = Image.new('RGB', (500, 500))
image.putdata([(g.get(x,y)*20, g.get(x,y)*20, g.get(x,y)*20) for y in range(500) for x in range(500)])

for x,y in c[-1][-1][1]:
    image.putpixel((y,x),(g.get(x,y)*20, g.get(x,y)*20, g.get(x,y)*20+70))
image = image.resize((1000,1000),Image.NEAREST)
image.save("15.png")
