from sys import stdin
from time import sleep
from aocd import get_data, submit
from re import findall

ls = stdin.read().split('\n')
r = set()
w = set()
ca = set()
for y in range(len(ls)):
    for x in range(len(ls[y])):
        c = ls[y][x]
        if c == '^':
            p = (x,y)
        elif c == '#':
            w.add((x,y))
        else:
            ca.add((x,y))

d = (0,-1)
print(p)
print(w)

def turn(d, x, y):
    match d:
        case (0,-1):
            return (1,0), x+1, y+1
        case (1,0):
            return (0,1), x-1, y+1
        case (0,1):
            return (-1,0), x-1, y-1
        case (-1,0):
            return (0,-1), x+1, y-1

def go(w):
    global d,p
    while True:
        x, y = p
        x += d[0]
        y += d[1]
        #print(x,y,d)
        if (x,y) in w:
            d, x, y = turn(d,x,y)
        if (x,y) in w:
            d, x, y = turn(d,x,y)

        if x < 0 or y < 0 or x >= len(ls[0]) or y >= len(ls):
            return False
        if False:
            for y1 in range(len(ls)):
                for x1 in range(len(ls[y1])):
                    if (x1,y1) in [rr[0] for rr in r]:
                        print('X', end='')
                    elif (x1,y1) in w:
                        print('#', end='')
                    else:
                        print(ls[y1][x1], end='')
                print()
            print()
        #print(x,y)
        p = (x,y)
        if (p,d) in r:
            return True
        r.add((p,d))

        #sleep(.2)

s = 0
for cc in ca:
    p1 = p
    d1 = d
    r = set()
    #print(cc)
    w.add(cc)
    if go(w):
        print(cc)
        s += 1
    if False:
        for y1 in range(len(ls)):
            for x1 in range(len(ls[y1])):
                if (x1,y1) in [rr[0] for rr in r]:
                    print('X', end='')
                elif (x1,y1) in w:
                    print('O' if (x1,y1) == cc else '#', end='')
                else:
                    print(ls[y1][x1], end='')
            print()
        print()
    #else: print('no', cc)
    p = p1
    d = d1
    w.remove(cc)

#print(r)
print(s)
