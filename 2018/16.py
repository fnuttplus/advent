from sys import stdin

def addr(r, a,b,c):
    r[c] = r[a] + r[b]
    return r
def addi(r, a,b,c):
    r[c] = r[a] + b
    return r
def mulr(r, a,b,c):
    r[c] = r[a] * r[b]
    return r
def muli(r, a,b,c):
    r[c] = r[a] * b
    return r
def banr(r, a,b,c):
    r[c] = r[a] & r[b]
    return r
def bani(r, a,b,c):
    r[c] = r[a] & b
    return r
def borr(r, a,b,c):
    r[c] = r[a] | r[b]
    return r
def bori(r, a,b,c):
    r[c] = r[a] | b
    return r
def setr(r, a,b,c):
    r[c] = r[a]
    return r
def seti(r, a,b,c):
    r[c] = a
    return r
def gtir(r, a,b,c):
    r[c] = 1 if a > r[b] else 0
    return r
def gtri(r, a,b,c):
    r[c] = 1 if r[a] > b else 0
    return r
def gtrr(r, a,b,c):
    r[c] = 1 if r[a] > r[b] else 0
    return r
def eqir(r, a,b,c):
    r[c] = 1 if a == r[b] else 0
    return r
def eqri(r, a,b,c):
    r[c] = 1 if r[a] == b else 0
    return r
def eqrr(r, a,b,c):
    r[c] = 1 if r[a] == r[b] else 0
    return r

fs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

d = {x: set([f.__name__ for f in fs]) for x in range(16)}
d = {0:gtir,1:setr,2:bori,3:gtrr,4:gtri,5:eqir,
     6:seti,7:eqri,8:eqrr,9:borr,10:addr,11:mulr,
     12:bani,13:muli,14:banr,15:addi}

print(d)

r = [0, 0, 0, 0]
for op, a,b,c in [map(int, line.split()) for line in stdin.read().splitlines()]:
    d[op](r, a,b,c)
    print(r)


"""
i = 0
while True:
    r0 = list(map(int, input()[9:-1].split(', ')))
    op, a,b,c = list(map(int, input().split()))
    r1 = list(map(int, input()[9:-1].split(', ')))
    j = 0
    s = set()
    for f in fs:
        f0 = f(r0[:], a,b,c)
        if f0 == r1:
            s.add(f.__name__)
            j += 1
    input()
    d[op] &= s
    if j >= 3:
        i += 1
        print(i, j)
    print(d)
"""
