from sys import stdin
from aocd import get_data, submit
from re import findall

#d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]

#grid = [list(x)+['.'] for x in stdin.read().splitlines()]

lines = stdin.read().splitlines()
ins = lines[0]

nodes = {}
for line in lines[2:]:
    a,b = line.split(' = ')
    nodes[a] = b[1:-1].split(', ')

print(nodes)

print(ins)
#for n in ['11A', '22A']:
for n in ['AAA', 'VLA', 'PJA', 'VSA', 'QKA', 'CPA']:
    s = 0
    been = {}
    while n not in been:
        been[n] = s
        for c in ins:
            #print(c, n)
            s += 1
            if c == 'L':
                n = nodes[n][0]
            if c == 'R':
                n = nodes[n][1]
            if n.endswith('Z'):
                print(n, s, s/263)
    print(n, s, been)


print(67*71*79*47*73*61*263)


a = list(filter(lambda x: x.endswith('A'), nodes.keys()))
print(a, all(s.endswith('A') for s in a))

s = 0

while not all(s.endswith('Z') for s in a):
    for c in ins:
        s += 1
        if c == 'L':
            for i in range(len(a)):
                a[i] = nodes[a[i]][0]
        if c == 'R':
            for i in range(len(a)):
                a[i] = nodes[a[i]][1]

print(s)