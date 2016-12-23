from sys import stdin

ins = [l.split() for l in stdin.read().splitlines()]

def toggle(i):
    if i >= len(ins): return
    if len(ins[i]) == 2:
        ins[i][0] = "dec" if ins[i][0] == "inc" else "inc"
    else:
        ins[i][0] = "cpy" if ins[i][0] == "jnz" else "jnz"

def val(v):
    try: return reg[v]
    except: return int(v)

ip = 0
reg = {a:0 for a in "abcd"}
reg["a"] = 7
while ip < len(ins):
    i = ins[ip]
    ip += 1
    if   i[0] == "cpy": reg[i[2]] = val(i[1])
    elif i[0] == "inc": reg[i[1]] += 1
    elif i[0] == "dec": reg[i[1]] -= 1
    elif i[0] == "jnz":
        if val(i[1]): ip += val(i[2])-1
    elif i[0] == "tgl": toggle(ip+val(i[1])-1)
print(reg["a"])

def f(x):
    if x is 2: return 2
    return x*f(x-1)

print(f(7) + 90*81)
print(f(12) + 90*81)
