from sys import stdin
from math import atan2, pi

a = set()
m = stdin.read().splitlines()

for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == "#":
            a.add((x,y))

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

aa = (11, 13)
t = []
i = 0
for bb in a:
    if aa == bb: continue
    for cc in a:
        if cc == bb or cc == aa: continue
        if dist(aa,cc)+dist(cc,bb)-dist(aa,bb)<1e-10: break
    else:
        i += 1
        t.append((pi-atan2(bb[0]-aa[0], bb[1]-aa[1]), bb))
print(i)
#print([sorted(t)[x-1][1] for x in [1,2,3,10,20,50,100,199,200,201]])
p = sorted(t)[199][1]
print(100*p[0]+p[1])
