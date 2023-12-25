from sys import stdin
from aocd import get_data, submit
from re import findall

#d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]

#grid = [list(x)+['.'] for x in stdin.read().splitlines()]

ss = 0
ww = {}
for line in stdin.read().splitlines():
    c, card = line.split(':')
    c = int(c[4:].strip())
    print('c', c)
    w,n  = card.split('|')
    w = [int(x) for x in findall('\d+', w)]
    n = [int(x) for x in findall('\d+', n)]
    a = 1
    s = 0
    for nn in n:
        if nn in w:
            #s = a
            s += 1
            #a *= 2
    if c in ww: ww[c] += 1
    else: ww[c] = 1
    for i in range(c+1, c+s+1):
        print(i)
        if i in ww:
            ww[i] += ww[c]
        else: ww[i] = ww[c]
    print('s', s)
    ss += s
    print(ww)
print(sum(ww.values()))

