depth = 4845
xt,yt = 6,770
m = [['.'] * 100 for _ in range(1000)]
y0 = [0]*101

for y in range(1000):
    for x in range(100):
        if (x == 0 and y == 0) or (x == xt and y == yt):
            gi = 0
        elif y == 0:
            gi = x*16807
        elif x == 0:
            gi = y*48271
        else:
            gi = x0 * y0[x]
        el = (gi+depth)%20183
        x0 = el
        y0[x] = el

        m[y][x] = ".=|"[el % 3]

for mm in m: print(''.join([mmm for mmm in mm]))

#tools: 't', 'c', 'n'
#rocky, '.', wet '=', narow '|'
#'.' ('c', 't')
#'=' ('c', 'n')
#'|' ('t', 'n')
def swap(t, r):
    if r is '.':
        if t is 'c':
            return 't'
        return 'c'
    if r is '=':
        if t is 'c':
            return 'n'
        return 'c'
    if r is '|':
        if t is 't':
            return 'n'
        return 't'

mm = [[{'t':1e100, 'c':1e100, 'n':1e100} for _ in range(100)] for _ in range(1000)]


def append(ns, x, y, t, n):
    if mm[y][x][t] > n:
        mm[y][x][t] = n
        ns.append((t, x, y, n))


s = [('t', 0,0 ,0)]
while s:
    ns = []
    for t, x,y, n in s:
        if yt == y and xt == x and t is 't':
            print(n)
        #print(y, x, t, n)
        r = m[y][x]
        dr = swap(t, r)
        if mm[y][x][dr] > n+7:
            mm[y][x][dr] = n+7

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            if 0 > x+dx or x+dx >= 100 or 0 > y+dy or y+dy >= 1000: continue
            dr = m[y+dy][x+dx]
            if r == dr:
                append(ns, x+dx, y+dy, t, n+1)
            else:
                if r is '.':
                    if dr is '=':
                        if t is 'c':
                            append(ns, x+dx, y+dy, t, n+1)
                        elif t is 't':
                            append(ns, x+dx, y+dy, 'c', n+8)
                    if dr is '|':
                        if t is 't':
                            append(ns, x+dx, y+dy, t, n+1)
                        elif t is 'c':
                            append(ns, x+dx, y+dy, 't', n+8)
                elif r is '=':
                    if dr is '.':
                        if t is 'c':
                            append(ns, x+dx, y+dy, t, n+1)
                        elif t is 'n':
                            append(ns, x+dx, y+dy, 'c', n+8)
                    if dr is '|':
                        if t is 'n':
                            append(ns, x+dx, y+dy, t, n+1)
                        elif t is 'c':
                            append(ns, x+dx, y+dy, 'n', n+8)
                elif r is '|':
                    if dr is '.':
                        if t is 't':
                            append(ns, x+dx, y+dy, t, n+1)
                        elif t is 'n':
                            append(ns, x+dx, y+dy, 't', n+8)
                    if dr is '=':
                        if t is 'n':
                            append(ns, x+dx, y+dy, t, n+1)
                        elif t is 't':
                            append(ns, x+dx, y+dy, 'n', n+8)

    s = sorted(ns, key=lambda tup: tup[3])

for y in mm:
    print(y)

print(mm[yt][xt]['t'])