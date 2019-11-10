from sys import stdin
from tools import gss

d = [[int(l[10:16]),  int(l[18:24]), int(l[36:38]), int(l[40:42])] for l in stdin.read().splitlines()]
def m(i):
    a = [x[0] + i*x[2] for x in d]
    return max(a) - min(a)

i = gss(m, 0, 100000, 0.4)
#while m(i+1) < m(i): i+=1
print(i)

for p in d:
    p[0] += i*p[2]
    p[1] += i*p[3]

dy = [y[1] for y in d]
dx = [x[0] for x in d]
for y in range(min(dy), max(dy)+1):
    print(''.join(["#" if (x,y) in [(i[0],i[1]) for i in d] else " " for x in range(min(dx),max(dx)+1)]))
