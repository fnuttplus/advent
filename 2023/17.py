from sys import stdin
from re import findall
from aoc import Grid
import heapq

g = Grid().from_stdin()
gc = (10e10,[])
s = [(0,0,0,(0,1),0,[])]
visited = {}
while s:
    n,x,y,d,c,path = s.pop(0)
    #dd = [d,(d[1], d[0]),(-d[1], -d[0])] if c > 3 else [d]
    dd = [d,(d[1], d[0]),(-d[1], -d[0])]
    for dx,dy in dd:
        if not g.fit(x+dx, y+dy): continue
        if d == (dx,dy): c1 = c+1
        else: c1 = 1
        #if c1 > 10: continue
        if c1 > 3: continue
        m = int(g[x+dx,y+dy])
        if (x+dx, y+dy, (dx, dy), c1) in visited:
            if visited[(x+dx, y+dy, (dx, dy), c1)] > n+m:
                visited[(x+dx, y+dy, (dx, dy), c1)] = n+m
            else: continue
        else:
            visited[(x+dx, y+dy, (dx, dy), c1)] = n+m
        heapq.heappush(s, (n + m, x+dx, y+dy, (dx, dy), c1,path + [(dx,dy)]))
        #if (x+dx, y+dy) == (g.x()-1,g.y()-1) and gc[0] > n+m and c1 >= 4: gc = (n+m, path)
        if (x+dx, y+dy) == (g.x()-1,g.y()-1) and gc[0] > n+m: gc = (n+m, path)

print(gc[0])
#exit()
x,y = 0,0
g[x,y] = chr(64+int(g[x,y]))
for dx,dy in gc[1]:
    x += dx
    y += dy
    g[x,y] = chr(64+int(g[x,y]))
    """
    g[x,y] = {
        (0,1): 'v',
        (0,-1): '^',
        (1,0): '>',
        (-1,0): '<',
    }[(dx,dy)]
    """
#print(g)
g[g.x()-1,g.y()-1] = chr(64+int(g[g.x()-1,g.y()-1]))


from PIL import Image
image = Image.new('RGB', (g.x(), g.y()))
image.putdata(g.image_data({
    '#': (9, 38, 53),
    '1': (14, 43, 58),
    '2': (19, 48, 63),
    '3': (24, 53, 68),
    '4': (29, 58, 73),
    '5': (34, 63, 78),
    '6': (40, 69, 84),
    '7': (45, 74, 89),
    '8': (50, 79, 94),
    '9': (55, 84, 99),
    'A': (58, 31, 14),
    'B': (63, 36, 19),
    'C': (68, 41, 24),
    'D': (73, 46, 29),
    'E': (78, 51, 34),
    'F': (84, 57, 40),
    'G': (89, 62, 45),
    'H': (94, 67, 50),
    'I': (99, 72, 55),
    '>': (9, 38, 53),
    'v': (9, 38, 53),
    '^': (9, 38, 53),
    '+': (158, 200, 185)
}))
image2 = image.resize((6*g.x(), 6*g.y()), Image.Resampling.NEAREST)
image2.save(f"2023.17a.png")
