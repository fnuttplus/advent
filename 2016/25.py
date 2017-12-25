def a(cb):
    d = cb
    a = 0
    while cb:
        cb >>= 2
        a = (a << 2) | 2
    return a-d
print(a(633*4))

from sys import stdin
ins = [l.split() for l in stdin.read().splitlines()]

def val(v): return reg[v] if v in reg else int(v)

ip = 0
reg = {a:0 for a in "abcde"}
while ip < len(ins):
    i,a,b = ins[ip][0],ins[ip][1],ins[ip][-1]
    ip += 1
    if   i == "cpy": reg[b] = val(a)
    elif i == "inc": reg[a] += 1
    elif i == "dec": reg[a] -= 1
    elif i == "jnz" and val(a): ip += val(b)-1
    elif i == "out": print(val(a))
