from sys import stdin

g  = [list(line) for line in stdin.read().splitlines()]

d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]
def adj(x,y):
    global g
    c = {"#": 0, "|": 0, ".": 0, }
    for dy, dx in d:
        if 0<=y+dy < 50 and 0 <= x+dx < 50:
            c[g[y+dy][x+dx]] += 1
    return c

s = [0] * 1000
for i in range(1000):
    if i % 10000000==0: print(i)
    o = []
    t = []
    l = []
    for y in range(len(g)):
        for x in range(len(g[y])):
            a = adj(x,y)
            if g[y][x] is '.' and a['|'] >= 3:
                t.append((x,y))
            if g[y][x] is '|' and a['#'] >= 3:
                l.append((x,y))
            if g[y][x] is '#' and not (a['|'] >= 1 and a['#'] >= 1):
                o.append((x,y))
        print(''.join(g[y]))
    for x,y in o:
        g[y][x] = '.'
    for x,y in t:
        g[y][x] = '|'
    for x,y in l:
        g[y][x] = '#'
    print()

    l = 0
    w = 0
    for y in range(len(g)):
        l += g[y].count("#")
        w += g[y].count("|")
    s[i] = l*w
    print(i,l*w,s[(i-399)%28+399])
