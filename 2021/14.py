from sys import stdin
#from aocd import lines, submit

lines = stdin.read().split("\n\n")
ins = lines[1].splitlines()
t = lines[0]

ins = {a.split(' -> ')[0]:a.split(' -> ')[1] for a in ins}
print(ins)
print(t)

pairs = {}

def insert(p, n):
    if p in pairs:
        pairs[p] += n
    else:
        pairs[p] = n

for i in range(len(t)-1):
    insert(t[i] + t[i+1], 1)

for x in range(40):
    change = []
    for p in pairs:
        if pairs[p] < 1: continue
        if p in ins:            
            change.append((pairs[p], p[0]+ins[p], ins[p]+p[1]))
            pairs[p] = 0
    #print(change)
    for a,b,c in change:
        insert(b, a)
        insert(c, a)
    #print(pairs)

c = {}
for p in pairs:
    if p[0] in c:
        c[p[0]] += pairs[p]
    else:
        c[p[0]] = pairs[p]
    if p[1] in c:
        c[p[1]] += pairs[p]
    else:
        c[p[1]] = pairs[p]

mx = 0
mn = 10e100
for a in c:
    if (c[a]+1)//2 > mx: mx = (c[a]+1)//2
    if (c[a]+1)//2 < mn: mn = (c[a]+1)//2
print(int(mx-mn))
