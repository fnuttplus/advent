from sys import stdin
from re import findall
from aoc import Grid
from copy import deepcopy as copy
#from aocd import submit
import heapq
import time

"""
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
Wolfram: Solve[{
    (19 + t1 (-2)) + a (t3 - t1) == (18 + t2 (-1)) + a (t3 - t2) == 20 + t3 (-2),
    (13 + t1 1) + b (t3 - t1) == (19 + t2 (-1)) + b (t3 - t2) == 25 + t3 (-2),
    (30 + t1 (-2)) + c (t3 - t1) == (22 + t2 (-2)) + c (t3 - t2) == 34 + t3 (-4)
}]
{{a->-3,b->1,c->2,t1->5,t2->3,t3->4}}
"""
px, py, pz = 19, 13, 30
vx, vy, vz = -2, 1, -2

a,b,c,t1 = -3,1,2,5
print((px +vx*t1 -a*t1), (py +vy*t1 -b*t1), (pz +vz*t1 -c*t1))

"""
246694783951603, 201349632539530, 307741668306846 @ 54, -21, 12
220339749104883, 131993821472398, 381979584524072 @ 77, 7, -58
148729713759711, 225554040514665, 96860758795727 @ 238, 84, 360
Solve[{
    (246694783951603 + t1 (54)) + a (t3 - t1) == (220339749104883 + t2 (77)) + a (t3 - t2) == 148729713759711 + t3 (238),
    (201349632539530 + t1 (-21)) + b (t3 - t1) == (131993821472398 + t2 (7)) + b (t3 - t2) == 225554040514665 + t3 (84),
    (307741668306846 + t1 (12)) + c (t3 - t1) == (381979584524072 + t2 (-58)) + c (t3 - t2) == 96860758795727 + t3 (360)
}]
{{a->26,b->-331,c->53,t1->846337127918,t2->981421067224,t3->573879763083}}
"""
a,b,c,t1 = 26,-331,53,846337127918

px,py,pz = 246694783951603, 201349632539530, 307741668306846
vx,vy,vz = 54, -21, 12
print((px +vx*t1 -a*t1) + (py +vy*t1 -b*t1) + (pz +vz*t1 -c*t1))

exit()
#part1
lines = stdin.read().splitlines()
hs = []
for line in lines:
    a,b = line.split(' @ ')
    s,d,f = map(int,a.split(','))
    g,h,j = map(int,b.split(', '))
    hs.append(((s,d,f),(g,h,j)))

#https://rosettacode.org/wiki/Find_the_intersection_of_two_lines#Python
def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    """ returns a (x, y) tuple or None if there is no intersection """
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)

    return x, y

s = 0
for a in hs:
    for b in hs:
        if a == b: continue
        pt = line_intersect(a[0][0], a[0][1], a[0][0] + 10**100*a[1][0], a[0][1] + 10**100*a[1][1],
                            b[0][0], b[0][1], b[0][0] + 10**100*b[1][0], b[0][1] + 10**100*b[1][1], )
        #print(a,b,pt)
        if pt != None and 200000000000000 <= pt[0] <= 400000000000000 and 200000000000000 <= pt[1] <= 400000000000000:
            s += 1
            #print('yes')
print(s//2)
