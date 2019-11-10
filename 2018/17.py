from sys import stdin, setrecursionlimit
setrecursionlimit(3000)
water = [500, 0]

m = [['.'] * 5000 for _ in range(5000)]

minx, maxx = 1000,0
miny, maxy = 100,0

for line in stdin.read().splitlines():
    if line[0] is 'y':
        y = int(line.split(', ')[0][2:])
        x0, x1 = map(int, line.split(', ')[1][2:].split('..'))
        for x in range(x0, x1+1):
            m[y][x] = '#'
        if x0 < minx: minx = x0
    else:
        x = int(line.split(',')[0][2:])
        y0, y1 = map(int, line.split(', ')[1][2:].split('..'))
        for y in range(y0, y1+1):
            m[y][x] = '#'
        if y0 < miny: miny = y0

    if x < minx: minx = x
    if x > maxx: maxx = x
    if y < miny: miny = y
    if y > maxy: maxy = y

def drop(x,y):
    if y > maxy: return
    if m[y+1][x] is '.':
        m[y][x] = '|'
        drop(x, y+1)
    if m[y+1][x] in '#~':
        v = [x]
        x1 = x - 1
        lwall, rwall = True, True
        while m[y+1][x1] in '#~' and m[y][x1] is '.':
            v.append(x1)
            x1 -= 1
        if m[y+1][x1] is '.':
            drop(x1, y)
            if not m[y][x1] in '#~':
                lwall = False

        x1 = x + 1
        while m[y+1][x1] in '#~' and m[y][x1] is '.':
            v.append(x1)
            x1 += 1
        if m[y+1][x1] is '.':
            drop(x1, y)
            if not m[y][x1] in '#~':
                rwall = False

        for x1 in v:
            m[y][x1] = '~' if rwall and lwall else '|'
    elif m[y+1][x] is '|':
        m[y][x] = '|'
    #for mm in m[maxy-20:maxy+1]: print(''.join(mm[minx-1:maxx+2]))


m[0][500] = '+'
drop(500,1)

c = 0
for mm in m[miny:maxy + 1]:
    s = ''.join(mm[minx-1:maxx+2])
    c += s.count('~')# + s.count('|')
    print(s)

print(minx, maxx, miny, maxy)
print(c)