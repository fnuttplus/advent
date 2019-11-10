from sys import stdin

ym = [1e1000000, -1e1000000]
xm = [1e1000000, -1e1000000]
zm = [1e1000000, -1e1000000]
n = []
for l in stdin.read().splitlines():
    ls = l.split(', ')
    x,y,z = map(int, ls[0][5:-1].split(','))
    r = int(ls[1][2:])
    n.append((x,y,z,r))

    if x < xm[0]:
        xm[0] = x
    if x > xm[1]:
        xm[1] = x
    if y < ym[0]:
        ym[0] = y
    if y > ym[1]:
        ym[1] = y
    if z < zm[0]:
        zm[0] = z
    if z > zm[1]:
        zm[1] = z
    
print(ym, xm, zm)

"""
mrn = [0,0,0,0]
for i in range(len(n)):
    nn = n[i]
    if nn[3] > mrn[3]:
        mrn = nn[:]
        mri = i

c = 0
for nn in n:
    if abs(nn[0]-mrn[0]) + abs(nn[1]-mrn[1]) + abs(nn[2]-mrn[2]) <= mrn[3]:
        c += 1
print(mrn, mri, c)
"""
s = 1
x = 59582782
y = 21741500
z = 23176750
for dx in range(10):
    print(x, y, z)
    for dy in range(10):
        for dz in range(10):
            j = 0
            for i in range(len(n)):
                a = n[i]
                if abs(a[0]-(x+dx)) + abs(a[1]-(y+dy)) + abs(a[2]-(z+dz)) <= a[3]:
                    j += 1
            print('({} {:3d})'.format((x+dx) + (y+dy) + (z+dz), j), end=' ')
        print()
    print()
