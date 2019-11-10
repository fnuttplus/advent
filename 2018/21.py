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
d = {f.__name__: f for f in fs}

ipr = int(input().split()[1])
ins = [line.split() for line in stdin.read().splitlines()]

r = [0, 0, 0, 0, 0, 0]
ip = r[ipr]
while 0 <= ip < len(ins):
    op, a,b,c = ins[ip]
    a,b,c = map(int, [a,b,c])
    d[op](r, a,b,c)
    if ip == 28: break
    r[ipr] += 1
    ip = r[ipr]
print(r[4])


h = []
r4 = 0
while True:
    r1 = r4 | 0x10000
    r4 = 2024736
    while True:
        r4 = ((((r1 & 0xFF) + r4) & 0xFFFFFF) * 65899) & 0xFFFFFF
        if 256 > r1: break
        r1 >>= 8

    if r4 in h:
        print(h[-1])
        break
    h.append(r4)
