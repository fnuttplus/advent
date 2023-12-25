from sys import stdin
from re import findall
from aoc import Grid

g = Grid().from_stdin()

i = 0
def sol(l):
    global i
    global image
    light = set()
    while l:
        nl = set()
        for b in l:
            x,y,d = b
            light.add((x,y,d))
            nd = [d]
            if g[x,y] == '.':
                pass
            elif g[x,y] == '\\':
                nd = [(d[1], d[0])]
            elif g[x,y] == '/':
                nd = [(-d[1], -d[0])]
            elif g[x,y] == '|':
                if d == (0,1) or d == (0,-1):
                    pass
                else:
                    nd = ((d[1], d[0]), (-d[1], -d[0]))
            elif g[x,y] == '-':
                if d == (1,0) or d == (-1,0):
                    pass
                else:
                    nd = ((d[1], d[0]), (-d[1], -d[0]))
            for dd in nd:
                dx,dy = dd
                if g.fit(x + dx,y + dy) and not (x + dx,y + dy,dd) in light:
                    nl.add((x + dx,y + dy,dd))
        l = list(nl)
        i += 1

        gc = Grid([list(x) for x in str(g).splitlines()])
        for x,y in gc.xy():
            if gc[x,y] in '|-\\/':
                gc[x,y] = 'O'
        for li in light:
            x,y,d = li
            #gc[x,y] = '#'
            #continue
            if type(gc[x,y]) is int:
                gc[x,y] += 1
            else:
                gc[x,y] = 1
                """
            elif gc[x,y] in '|-\\/':
                pass
            elif gc[x,y] in '<>^v':
                gc[x,y] = 2
            else:
                gc[x,y] = {
                    (0,1): 'v',
                    (0,-1): '^',
                    (1,0): '>',
                    (-1,0): '<',
                }[d]
                """
        #print(gc)
        print(i)
        image.putdata(gc.image_data({'.': (9, 38, 53), 1: (92, 131, 116), 2: (117, 156, 141), 3: (143, 182, 167), 4: (168, 207, 192), 'O': (27, 66, 66), '+': (158, 200, 185)}))
        image2 = image.resize((8*g.x(), 8*g.y()), Image.Resampling.NEAREST)
        image2.save(f"frames/2023.16.{i}.png")

    #for x,y,d in light: g[x,y] = '#'
    return len(set([(x,y) for x,y,_ in light]))
#print(sol([(0,0,(1,0))]))
from PIL import Image
image = Image.new('RGB', (g.x(), g.y()))
print(sol([(109, 93, (-1, 0))]))


exit()
m = 0
for x in range(g.x()):
    s = sol([(x,0,(0,1))])
    if s > m:
        print((x,0,(0,1)))
        m = s
    s = sol([(x,g.y()-1,(0,-1))])
    if s > m:
        print((x,g.y()-1,(0,-1)))
        m = s
for y in range(g.y()):
    s = sol([(0,y,(1,0))])
    if s > m:
        print((0,y,(1,0)))
        m = s
    s = sol([(g.x()-1,y,(-1,0))])
    if s > m:
        print((g.x()-1,y,(-1,0)))
        m = s
print(m)