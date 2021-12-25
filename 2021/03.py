from sys import stdin
#from aocd import lines, submit

lines = stdin.read().splitlines()

def ogr(l,n):
    c = [0]*len(l[0])
    for ll in l:
    #    print(l)
        g = list(ll)
    #    print(g)
        for i in range(len(g)):
            c[i] += int(g[i])
    #print(n, c[n], )
    return 1 if c[n] >= len(l)/2 else 0

def cgr(l,n):
    c = [0]*len(l[0])
    for ll in l:
    #    print(l)
        g = list(ll)
    #    print(g)
        for i in range(len(g)):
            c[i] += int(g[i])
    return 0 if c[n] >= len(l)/2 else 1

def subl(l,n,i):
    for ll in l:
        if ll[n] == str(i):
            yield ll

ol = lines
cl = lines
for i in range(len(lines[0])):
    o = ogr(ol,i)
    c = cgr(cl,i)
    if len(ol) > 1:
        ol = list(subl(ol,i,o))
    if len(cl) > 1:
        cl = list(subl(cl,i,c))
    #print(o, ol)
    #print(c, cl)

print(int(ol[0], 2) * int(cl[0], 2))
