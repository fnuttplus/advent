from sys import stdin
from re import findall
from aoc import Grid
from copy import deepcopy as copy
import heapq
import time


#g = Grid().from_stdin()
#gc = [[g.copy() for _ in range(5)] for _ in range(5)]

lines = stdin.read().splitlines()

bricks = []

#brick x,y,z
#ground z=0
jenga = [[[-1 for _ in range(10)] for _ in range(10)] for _ in range(325)]

i = -1
for brick in lines:
    i += 1
    a,b = brick.split('~')
    brick = [list(map(int, a.split(','))), list(map(int, b.split(',')))]
    bricks.append(brick)
    a,b = brick
    for x in range(a[0], b[0]+1):
      for y in range(a[1], b[1]+1):
        for z in range(a[2], b[2]+1):
          assert(jenga[z][y][x] == -1)
          jenga[z][y][x] = i

#print(jenga)

def canmove(brick):
  x0,y0,z0 = brick[0]
  x1,y1,z1 = brick[1]
  if z0-1 == 0: return False
  for x in range(x0, x1+1):
    for y in range(y0, y1+1):
      if jenga[z0-1][y][x] != -1:
        return False
  return True

def move(brick, n):
  x0,y0,z0 = brick[0]
  x1,y1,z1 = brick[1]
  for x in range(x0, x1+1):
    for y in range(y0, y1+1):
        for z in range(z0, z1+1):
            jenga[z][y][x] = n

def supports(brick):
    print(brick)
    s = set([-1])
    x0,y0,z0 = brick[0]
    x1,y1,z1 = brick[1]
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            print(z1+1,y, x, jenga[z1+1][y][x])
            s.add(jenga[z1+1][y][x])
    s.remove(-1)
    return s

def gravity():
    anythinghasmoved = True
    s = set()
    while anythinghasmoved:
        anythinghasmoved = False
        for i, brick in enumerate(bricks):
            if canmove(brick):
                anythinghasmoved = True
                move(brick, -1)
                bricks[i][0][2] -= 1
                bricks[i][1][2] -= 1
                move(brick, i)
                s.add(i)
    return s
gravity()
"""
for i, brick in enumerate(bricks):
   #print(i, brick)
   r = (i + 333) // (12*12)
   g = ((i + 333) % (12*12)) // 12
   b = (i + 333) % 12
   #print((r+1)/12,g,b)
   print(f'draw_affine_parallelepiped(vec3({brick[0][0]}., {brick[0][1]}., {brick[0][2]}.), {0.9999 + brick[1][0] - brick[0][0]}*Vec3::X, {0.9999 + brick[1][1] - brick[0][1]} * Vec3::Y, {0.9999 + brick[1][2] - brick[0][2]} * Vec3::Z, None, Color::new({(r+1)/12}, {(g+1)/12}, {(b+1)/12}, 1.0));')
exit()
#print(jenga)
"""
"""
for z in range(100, 0, -1):
    for x in range(10):
        y = set([jenga[z][y][x] for y in range(3)])
        if -1 in y: y.remove(-1)
        if len(y) == 0: print('.'.rjust(7),end='')
        if len(y) == 1: print(str(y).rjust(7),end='')
        if len(y) > 1: print('?'.rjust(7),end='')
    print()
print()
for z in range(100, 0, -1):
    for x in range(10):
        y = set([jenga[z][x][y] for y in range(3)])
        if -1 in y: y.remove(-1)
        if len(y) == 0: print('.'.rjust(7),end='')
        if len(y) == 1: print(str(y).rjust(7),end='')
        if len(y) > 1: print('?'.rjust(7),end='')
    print()
"""

def collapse(i):
    global jenga
    brick = bricks[i]
    s = supports(brick)
    #print(s)
    move(brick, -1)
    for i in list(s):
        if not canmove(bricks[i]):
            s.remove(i)
    for i in list(s):
       move(bricks[i], -1)
    #print(s)
    return s

s1 = 0
s2 = 0
for i in range(len(bricks)):
    jenga_copy = copy(jenga)
    move(bricks[i], -1)
    bricks_copy = copy(bricks)
    bricks = bricks[:i] + bricks[i+1:]
    m = gravity()
    jenga = copy(jenga_copy)
    bricks = copy(bricks_copy)
    if len(m) > 0:
        #print(i, 'cannot', len(m))
        s2 += len(m)
    else:
        s1 += 1
        #print(i, 'can')
print(s1, s2)
