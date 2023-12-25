from sys import stdin
from re import findall
from aoc import Grid
import heapq
import time

n = (26501365 - 65) // 131
print(
  7362 * (n-1)*(n-1)
+ 7354 * n*n
+ 5541 + 5538 + 5555 + 5558
+ (925 + 937 + 941 + 936) * n
+ (6459 + 6444 + 6456 + 6461) * (n-1)
)
#602259568764234

g = Grid().from_stdin()
gc = [[g.copy() for _ in range(5)] for _ in range(5)]

#sx,sy = g.find('S')
#print(sx, sy, g.x(), g.y())
sx = 65+131*2
sy = 65+131*2
q = [(sx, sy, 0)]
memo = set()
while q:
    x, y, s = q.pop()
    memo.add((x,y,s))
    gx,gy = x//131, y//131
    if s == 65+131*2:
        gc[gy][gx][x%131, y%131] = 'O'
        continue
    for x1,y1 in [(x+1, y),(x-1, y),(x, y+1),(x, y-1),]:
        if 0 <= x1 < 131*5 and 0 <= y1 < 131*5 and gc[gy][gx][x1%131, y1%131] in '.OS' and (x1,y1,s+1) not in memo:
            q.append((x1,y1,s+1))

"""
for y in range(5):
    print()
    for x in range(5):
        gc[y][x].save_image_file({
            '#': (92, 131, 116),
            '.': (9, 38, 53),
            'O': (27, 66, 66),
            'S': (9, 38, 53)
        }, f'2023.21.{x}-{y}.png')
        print(str(gc[y][x].count('O')).rjust(6), end='')
"""
c = [[gc[y][x].count('O') for x in range(5)] for y in range(5)]

n = (26501365 - 65) // 131
print(
  c[2][2] * (n-1)*(n-1)
+ c[1][2] * n*n
+ c[0][2] + c[2][4] + c[4][2] + c[2][0]
+ (c[0][1] + c[0][3] + c[3][4] + c[3][0]) * n
+ (c[1][1] + c[1][3] + c[3][3] + c[3][1]) * (n-1)
)
"""
   0   925  5541   937     0
 925  6459  7354  6444   937
5558  7354  7362  7354  5538
 936  6461  7354  6456   941
   0   936  5555   941     0

n = 2
  eaf
 ei0jf
 d010b
 hl0kg
  hcg

n = 4
   eaf
  ei0jf
 ei010jf
ei01010jf
d0101010b
hl01010kg
 hl010kg
  hl0kg
   hcg

0 = 7354 * n*n
1 = 7362 * (n-1)*(n-1)
a = 5541 * 1
b = 5538 * 1
c = 5555 * 1
d = 5558 * 1
e = 925 * n
f = 937 * n
g = 941 * n
h = 936 * n
i = 6459 * (n-1)
j = 6444 * (n-1)
k = 6456 * (n-1)
l = 6461 * (n-1)

"""
