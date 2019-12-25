from sys import stdin
m0 = [[c for c in line] for line in stdin.read().splitlines()]
m = m0[:]
d = {}
dat = []
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == '@':
            dat.append((x,y))
        elif not m[y][x] in "#.":
            d[m[y][x]] = (x,y)

dA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ka = "abcdefghijklmnopqrstuvwxyz"
#print(dat)

def bfs(d, m):
    x,y = d
    s = [(x,y,0,set(),[])]
    m[y][x] = "#"
    dd = ((0,-1),(0,1),(-1,0),(1,0))
    k = {}
    while s:
        x,y,i,d,p = s.pop(0)
        for dx,dy in dd:
            mm = m[y+dy][x+dx]
            m[y+dy][x+dx] = "#"
            if mm in dA:
                s.append((x+dx, y+dy, i+1, d|{mm}, p+[(x+dx,y+dy)]))
            elif mm in ka:
                k[mm.upper()] = (i+1, d, p+[(x+dx,y+dy)])
                s.append((x+dx, y+dy, i+1, d, p+[(x+dx,y+dy)]))
            elif mm == ".":
                s.append((x+dx, y+dy, i+1, d, p+[(x+dx,y+dy)]))
    return k

kd = {k.upper():bfs(d[k], [r[:] for r in m0]) for k in ka}
kdat = [bfs(at, [r[:] for r in m0]) for at in dat]
#for k in kdat: print(k)
#for k in kd: print(k, kd[k])

from PIL import Image
def color2(a):
    if a in "aA": return (0, 0, 180)
    if a in "bB": return (175, 13, 102)
    if a in "cC": return (146,248,70)
    if a in "dD": return (255, 200, 47)
    if a in "eE": return (255,118,0)
    if a in "fF": return (185,185,185)
    if a in "gG": return (235,235,222)
    if a in "hH": return (100,100,100)
    if a in "iI": return (255,255,0)
    if a in "jJ": return (55,19,112)
    if a in "kK": return (255,255,150)
    if a in "lL": return (202,62,94)
    if a in "mM": return (205,145,63)
    if a in "nN": return (12,75,100)
    if a in "oO": return (255,0,0)
    if a in "pP": return (175,155,50)
    if a in "qQ": return (0,0,0)
    if a in "rR": return (37,70,25)
    if a in "sS": return (121,33,135)
    if a in "tT": return (83,140,208)
    if a in "uU": return (0,154,37)
    if a in "vV": return (178,220,205)
    if a in "wW": return (255,152,213)
    if a in "xX": return (0,0,74)
    if a in "yY": return (175,200,74)
    if a in "zZ": return (63,25,12)

dd = [[1,1,1],[1,0,1],[1,1,1]]
def color(x,y):
    if m0[y//3][x//3] == "@":
        return (110, 110, 110)
    if m0[y//3][x//3] in ka:#keys
        if dd[y%3][x%3] == 1:
            return (240,240,240)
        return color2(m0[y//3][x//3])
    if m0[y//3][x//3] in dA:#doors
        if dd[y%3][x%3] == 1:
            return color2(m0[y//3][x//3])
        return (240,240,240)
    if m0[y//3][x//3] == ".":
        return (240,240,240)
    return (0,0,0)

j = 0
for c in "OCNKERJIQDZVTYHWBXUFMASLGP":
    for i in range(4):
        if c in kdat[i]:
            print(i, d[c])
            for x,y in kdat[i][c][2]:
                print(dat[i])
                m0[y][x] = "@"
                m0[dat[i][1]][dat[i][0]] = "."
                dat[i] = (x,y)
                image = Image.new('RGB', (81*3, 81*3))
                image.putdata([color(x,y) for y in range(81*3) for x in range(81*3)])
                image = image.resize((81*3*4,81*3*4), Image.NEAREST)
                image.save("frames/advent18b_"+str(j)+".png")
                j += 1
            kdat[i] = kd[c]
    x,y = d[c]
    m0[y][x] = "."
    image = Image.new('RGB', (81*3, 81*3))
    image.putdata([color(x,y) for y in range(81*3) for x in range(81*3)])
    image = image.resize((81*3*4,81*3*4), Image.NEAREST)
    image.save("frames/advent18b_"+str(j)+".png")
    j += 1
