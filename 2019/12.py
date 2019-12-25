from sys import stdin
m = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1], ]
m = [[int(x.split('=')[1][:-1]) for x in l.split(' ')] for l in stdin.read().splitlines()]
v = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],]
s = 0
vv = [0,0,0]
while 0 in vv:
    s += 1
    for i in range(len(m)):
        for j in range(i, len(m)):
            for x in range(3):
                if m[i][x] > m[j][x]:
                    v[i][x] -= 1
                    v[j][x] += 1
                elif m[i][x] < m[j][x]:
                    v[i][x] += 1
                    v[j][x] -= 1

    e = 0
    for i in range(len(m)):
        p = 0
        k = 0
        for x in range(3):
            m[i][x] += v[i][x]
            p += abs(m[i][x])
            k += abs(v[i][x])
        e += p*k
    if s == 1000: print("part 1:", e)

    for i in range(3):
        if vv[i] == 0:
            for x in v:
                if x[i] != 0: break
            else:
                vv[i] = s
print(vv)
print(vv[0]*vv[1]*vv[2])