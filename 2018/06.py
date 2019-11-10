from sys import stdin
from colorsys import hsv_to_rgb

coo = [tuple(map(int, l.split(', '))) for l in stdin.read().splitlines()]

ab = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
xy = [['']*400 for _ in range(400)]
for x in range(400):
    for y in range(400):
        r = 801
        for i in range(len(coo)):
            rr = abs(coo[i][0]-x) + abs(coo[i][1]-y)
            if rr < r:
                r = rr
                ri = ab[i]
            elif rr == r:
                ri = '.'
        xy[y][x] = ri

#for y in xy: print(''.join(y))
"""
a1 = "abcdefghijklmoL"
a2 = "npqrstuwxyz"
a3 = "ABCDEFGHIJKM"
a4 = "NOPQRSTUWXYZ"

def f(x):
    r,g,b = hsv_to_rgb(x/50, 1, 1)
    print(r,g,b)
    return (int(r*256),int(g*256),int(b*256))
    if x in a1: return (0,135,68) #green
    if x in a2: return (0,87,231) #blue
    if x in a3: return (214,45,32) #red
    if x in a4: return (255,167,0) #orange
    return (0, 0, 0)


from PIL import Image
image = Image.new('RGB', (400, 400))
image.putdata([(0,0,0) if xy[y][x] is '.' else f(ab.index(xy[y][x])) for y in range(400) for x in range(400)])
image = image.resize((1200,1200), Image.NEAREST)
image.save("advent6.png")

exit()
"""
b = {}
for a in ab:
    if a in xy[0]: continue
    if a in xy[-1]: continue
    if a in [y[0] for y in xy]: continue
    if a in [y[-1] for y in xy]: continue
    
    s = 0
    for y in xy:
        s += y.count(a)
    b[a] = s

#print(b)
print(max(b.values()))

p = 0
xy = [['']*400 for _ in range(400)]
for x in range(400):
    for y in range(400):
        s = 0
        for i in range(len(coo)):
            s += abs(coo[i][0]-x) + abs(coo[i][1]-y)
        xy[y][x] = 'x' if s < 10000 else '.'
        if s < 10000:
            p += 1

#for y in xy: print(''.join(y))
print(p)