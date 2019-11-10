from sys import stdin

ids = [l.split() for l in stdin.read().splitlines()]

m = [[set() for _ in range(1000)] for _ in range(1000)]
al = set()
for i in ids:
    a = int(i[0][1:])
    x,y = map(int, i[2][:-1].split(','))
    w,h = map(int, i[3].split('x'))

    for l in range(x, x+w):
        for j in range(y, y+h):
            m[l][j].add(a)
    al.add(a)

c = 0
for i in m:
    for j in i:
        if len(j) > 1:
            c +=1
            for jj in j:
                al.discard(jj)

print(c)
print(al)

#    print(a,x,y,w,h)
