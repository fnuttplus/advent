from sys import stdin
from aocd import get_data, submit
from re import findall

#d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]

#grid = [list(x)+['.'] for x in stdin.read().splitlines()]

#time = [7,15,30]
#dist = [9,40,200]
#time = [49,78,79,80]
#dist = [298,1185,1066,1181]
time = [49787980]
dist = [298118510661181]
#time = [71530]
#dist = [940200]

p = 1
for i in range(len(time)):
    t = time[i]
    d = dist[i]
    c = 0
    for n in range(0, t + 1, 1):
        dd = n * (t-n)
        #print(n, dd, d)
        if dd > d:
            c += 1
    p *= c
    #print(c)

print(p)
print(42826983 - 6960998)
exit()
p = 1
for i in range(len(time)):
    t = time[i]
    d = dist[i]
    c = 0
    for n in range(t + 1):
        dd = n * (t-n)
        #print(n, dd, d)
        if dd > d:
            c += 1
    p *= c
    #print(c)

print(p)
#Time:        49     78     79     80
#Distance:   298   1185   1066   1181

