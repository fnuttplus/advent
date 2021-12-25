from sys import stdin

def step(z, w, y):
    a,b,c = y
    x = 0 if z%26+a == w else 1
    return (25*x+1)*int(z/b) + (w+c)*x

dd = [
    (11, 1, 8),
    (12, 1, 8),
    (10, 1, 12),
    (-8, 26, 10),
    (15, 1, 2),
    (15, 1, 8),
    (-11, 26, 4),
    (10, 1, 9),
    (-3, 26, 10),
    (15, 1, 3),
    (-3, 26, 7),
    (-1, 26, 7),
    (-10, 26, 2),
    (-16, 26, 2),
]

memo = {}
def rec(z0, d):
    global m
    if (z0,d) in memo: return memo[(z0,d)]

    s = set()
    for w in range(1,10):
        z = step(z0, w, dd[d])
        if d == 13:
            if z == 0:
                s.add(str(w))
        else:
            for ss in rec(z, d+1):
                s.add(str(w) + ss)
    memo[(z0,d)] = s
    return s

#for r in (rec(0,0)): print(r)

l = stdin.read().splitlines()
print(max(l), min(l))
