from sys import stdin

data = stdin.read().splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

n = 200

for y in range(len(data)):
    for x in range(len(data[0])):
        grid[n+y][n+x] = 1 if data[y][x] is '#' else 0

x,y,d = n+len(data)//2, n+len(data)//2, 'u'

def turn(d, r):
    ds = 'urdl'
    return ds[(ds.index(d) + r) % len(ds)]

def move(x,y,d):
    if d is 'u': return x, y-1
    if d is 'd': return x, y+1
    if d is 'l': return x-1, y
    if d is 'r': return x+1, y

def change(s):
    ss = [0,2,1,3]
    return ss[(ss.index(s) + 1) % len(ss)]

i = 0
for j in range(10000000):
    if grid[y][x] == 2: i += 1
    elif grid[y][x] == 0: d = turn(d, -1)
    elif grid[y][x] == 1: d = turn(d, +1)
    elif grid[y][x] == 3: d = turn(turn(d, +1), +1)
    grid[y][x] = change(grid[y][x])
    x,y = move(x,y,d)
    
print(i)

s = '.#WF'

print('\n'.join([''.join([s[x] for x in grid[y][:200]]) for y in range(200)]))
#Langtons ant