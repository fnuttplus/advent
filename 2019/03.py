d = {'U':(0,-1),'D':(0,1),'L':(-1,0),'R':(1,0),}

x,y,i = 0,0,0
m = {(0, 0):0}
for w in input().split(','):
    dx,dy = d[w[0]]
    for _ in range(int(w[1:])):
        x += dx
        y += dy
        i += 1
        if (x,y) not in m:
            m[(x,y)] = i

x,y,i = 0,0,0
n = 10e10
for w in input().split(','):
    dx,dy = d[w[0]]
    for _ in range(int(w[1:])):
        x += dx
        y += dy
        i += 1
        if (x,y) in m:
            #n0 = abs(x) + abs(y)
            n0 = m[(x,y)] + i
            if n > n0:
                n = n0
print(n)
