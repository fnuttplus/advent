from sys import stdin
from aocd import get_data, submit
from re import findall

d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]

grid = [list(x)+['.'] for x in stdin.read().splitlines()]

def issymbol(c):
    return c not in '1234567890.'

def adj(x,y):
    for dx,dy in d:
        if (len(grid) > x+dx >= 0) and (len(grid[0]) > y+dy >= 0) and grid[x+dx][y+dy] == '*':
            return True, x+dx, y+dy
    return False, -1, -1

s = 0
print(grid)

store = {}
for x in range(len(grid)):
    line = grid[x]
    i = 0
    while i < len(line):
        n = 0
        c = line[i]
        a = False
        ggx,ggy = -1, -1
        while c.isnumeric():
            n = 10*n + int(c)
            aa, gx, gy = adj(x,i)
            if aa:
                a = True
                ggx = gx
                ggy = gy

            i += 1
            c = line[i]

        if a == True:
            print(n, ggx, ggy)
            if (ggx, ggy) in store:
                store[(ggx, ggy)].append(n)
            else:
                store[(ggx, ggy)] = [n]



        i += 1

print(store)

for gear in store:
    if len(store[gear]) == 2:
        s += store[gear][0] * store[gear][1]
print(s)
