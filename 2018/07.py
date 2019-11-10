from sys import stdin

lines = [l.split(' ') for l in stdin.read().splitlines()]

ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = {x: [] for x in ab}

for l in lines:
    a[l[7]].append(l[1])
#print(a)

"""
s = ""
while a:
    for b in a:
        if a[b] == []:
            a.pop(b)
            s += b
            for bb in a:
                if b in a[bb]: a[bb].remove(b)
            break
print(s)
"""
n = 5
w = {x: [0,'?'] for x in range(n)}
i = -1
s = ""
while a:
    for x in range(n):
        if w[x][0] == 0 and w[x][1] != '?':
            s += w[x][1]
            for bb in a:
                if w[x][1] in a[bb]: a[bb].remove(w[x][1])
            w[x] = [0, '?']

    cb = []
    for b in a:
        if a[b] == []:
            for x in range(n):
                if w[x][0] == 0:
                    w[x] = [61 + ab.index(b), b]
                    cb.append(b)
                    break
    for cc in cb:
        a.pop(cc)
            
    for x in range(n):
        if w[x][0] > 0 and w[x][1] != '?':
            w[x][0] -= 1
    i += 1
#    print(i, s, w)

print(i + max([x[0] for x in w.values()]) + 1)