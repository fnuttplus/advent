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

r = [0, 0, 0, 0, 0, 0]
ipr = int(input().split()[1])

def sum_divisors(n): return sum([i for i in range(1, n+1) if n % i == 0])
print(sum_divisors(900))
print(sum_divisors(10551300))

r0 = []
ins = [line.split() for line in stdin.read().splitlines()]
ip = r[ipr]
while 0 <= ip < len(ins):
    op, a,b,c = ins[ip]
    a,b,c = map(int, [a,b,c])
    d[op](r, a,b,c)
    if not r[0] in r0:
        print(ip, r)
        r0.append(r[0])
    r[ipr] += 1
    ip = r[ipr]
print(r)
