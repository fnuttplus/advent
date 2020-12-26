from sys import stdin


d = {}
tiles = {}
for s in stdin.read().split("\n\n"):
    g = s.split('\n')
    t = int(g[0].split(' ')[1][:-1])
    tiles[t] = g[1:]
    
    d[t] = [g[1]]
    d[t].append(g[1][::-1])

    d[t].append(''.join([x[-1] for x in g[1:]]))
    d[t].append(''.join([x[-1] for x in g[1:]][::-1]))

    d[t].append(g[-1][::-1])
    d[t].append(g[-1])

    d[t].append(''.join([x[0] for x in g[-1:0:-1]]))
    d[t].append(''.join([x[0] for x in g[1:]]))
#print(d)
e = {dd:set() for dd in d}
for dd in d:
    for xx in d:
        if dd == xx: continue
        for a in d[dd]:
            if a in d[xx]:
                #print(dd, xx, a)
                e[dd].add(xx)
n = 1
for ee in e:
    if len(e[ee]) == 2:
        #print(ee, e[ee])
        t0 = ee
        n *= ee
print("PART 1:", n)

def perm(t):
    for _ in range(4):
        t = [''.join([tt[i] for tt in t[::-1]]) for i in range(len(t[0]))]
        yield t
        yield t[::-1]

image = []
def draw(tile, ids):
    global image
    d = [t[1:-1] for t in tile[1:-1]]
    h = ''.join([t[-1] for t in tile])
    for x in range(12):
        for t in tiles:
            if t in ids: continue
            for p in perm(tiles[t]):
                if h == ''.join([t[0] for t in p]):
                    for i in range(len(d)):
                        d[i] += p[i+1][1:-1]
                    h = ''.join([t[-1] for t in p])
                    ids.add(t)
                    break
            else: continue
            break
    image += d
    for t in tiles:
        if t in ids: continue
        for p in perm(tiles[t]):
            if tile[-1] == p[0]:
                nt = p
                ids.add(t)
                break
        else: continue
        break
    else: return
    draw(nt, ids)

draw(tiles[t0], {t0})

monster = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   ",
]

def match(x, y):
    for z in range(len(monster)):
        for w in range(len(monster[0])):
            if monster[z][w] == "#" and image[y+z][x+w] != "#":
                return False
    return True

def overlap(x, y):
    for z in range(len(monster)):
        for w in range(len(monster[0])):
            if monster[z][w] == "#":
                r = list(image[y+z])
                r[x+w] = "O"
                image[y+z] = ''.join(r)

for image in perm(image):
    found = False
    for y in range(len(image) - len(monster)):
        for x in range(len(image[0]) - len(monster[0])):
            if match(x, y):
                found = True
                overlap(x, y)
    if found: break

#for row in image: print(row)
"""
from PIL import Image
png = Image.new('RGB', (len(image[0]), len(image)))
cc = {"#": (39,59,80), ".": (30,42,95), "O": (33,93,93)}
png.putdata([cc[ggg] for gg in image for ggg in gg])
png = png.resize((960,960), Image.NEAREST)
for y in range(0, 960, 80):
    for x in range(960):
        png.putpixel((x,y),(20,40,70))
        png.putpixel((y,x),(20,40,70))
for x in range(960):
    png.putpixel((x,959),(20,40,70))
    png.putpixel((959,x),(20,40,70))
png.save("frames/advent_20.png")
"""
n = sum(r.count("#") for r in image)
print("PART 2:", n)
