from sys import stdin
#from aocd import lines, submit

g = [[0 for x in range(1000)] for y in range(1000)]
lines = stdin.read().splitlines()
for line in lines:
    a,b = line.split(' -> ')
    x1,y1 = map(int, a.split(','))
    x2,y2 = map(int, b.split(','))
    if x1 > x2:
        x1,x2 = x2,x1
        y1,y2 = y2,y1

    if x1 == x2:
        if y1 > y2: y1,y2 = y2,y1
        for y in range(y1, y2+1):
            g[y][x1] += 1
    elif y1 == y2:
        for x in range(x1, x2+1):
            g[y1][x] += 1
    else:
        for d in range((x2-x1)+1):
            if y1 > y2:
                g[y1-d][x1+d] += 1
            else:
                g[y1+d][x1+d] += 1

n = 0
for x in range(1000):
    for y in range(1000):
        if g[y][x] > 1:
            n += 1
        #print(g[x][y], end=",")
    #print()
print(n)
