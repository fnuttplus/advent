from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations

s = 0

r = {}

t = True
t = False

ls = stdin.read() if t else get_data()
ls = [list(map(int, [-1 if ll == '.' else ll for ll in list(l)])) for l in ls.split('\n')]

print(ls)

ss = set()
for y in range(len(ls)):
    for x in range(len(ls[0])):
        if ls[y][x] == 0:
            ss.add((x,y))

if t: print(ss, len(ss))

def dfs(x0,y0):
    q = [(x0, y0)]
    while q:
        (x,y) = q.pop()
        if ls[y][x] == 9:
            print(x,y)
            yield (x,y)
        for x1,y1 in [(x+1, y),(x-1, y),(x, y+1),(x, y-1),]:
            if 0 <= x1 < len(ls[0]) and 0 <= y1 < len(ls) and ls[y1][x1] == ls[y][x] +1:
                q.append((x1,y1))

for p in ss:
    if t: print('a', p)
    if t: print(len(set(dfs(p[0],p[1]))))
    s += len(list(dfs(p[0],p[1])))


if t:
    print(s)
else:
    submit(s)
