from sys import stdin

ins = [l.split() for l in stdin.read().splitlines()]

def val(v):
	if v in reg: return reg[v]
	return int(v)

def is_prime(a): return all(a % i for i in range(2, a))

b = 57*100+100000
c = b + 17000
print(sum([1 if not is_prime(x) else 0 for x in range(b, c+1, 17)]))

reg = {a: 0 for a in 'abcdefgh'}
reg['a'] = 0
ip=0
count = 0
while ip < len(ins):
    i, x, y = ins[ip]
    ip += 1
    if ip == 26: print(ip, ins[ip], reg, is_prime(reg['b']))
    if   i == "set": reg[x] = val(y)
    elif i == "sub": reg[x] -= val(y)
    elif i == "mul":
        count += 1
        reg[x] *= val(y)
    elif i == "jnz":
        if val(x) != 0: ip += val(y)-1
print(count)
