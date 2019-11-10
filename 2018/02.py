from sys import stdin

ids = stdin.read().splitlines()

t2, t3 = 0, 0
ab = "abcdefghijklmnopqrstuvwxyz"

for i in ids:
    c2, c3 = True, True
    for a in ab:
        if c2 and i.count(a) == 2:
            t2 += 1
            c2 = False
        if c3 and i.count(a) == 3:
            t3 += 1
            c3 = False

print(t2 * t3)

for i in range(len(ids)):
    for j in range(i, len(ids)):
        c = 0
        for ii in range(len(ids[i])):
            if ids[i][ii] == ids[j][ii]:
                c += 1
            else:
                o = ii
        if c == ii:
            print(ids[i][:o] + ids[i][o+1:])
