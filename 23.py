from sys import stdin

ins = [l.split() for l in stdin.read().splitlines()]

def toggle(i):
    if i >= len(ins): return
    if len(ins[i]) == 2:
        ins[i][0] = "dec" if ins[i][0] == "inc" else "inc"
    else:
        ins[i][0] = "cpy" if ins[i][0] == "jnz" else "jnz"
    return ins[i]

def val(v):
    if v in reg: v = reg[v]
    else: v = int(v)
    return v

ip = 0
reg = {a:0 for a in "abcd"}
reg["a"] = 7
while ip < len(ins):
    line = ins[ip]
    ip += 1
    if line[0] == "cpy":
        reg[line[2]] = val(line[1])
    elif line[0] == "inc":
        reg[line[1]] += 1        
    elif line[0] == "dec":
        reg[line[1]] -= 1        
    elif line[0] == "jnz":
        if val(line[1]): ip += val(line[2])-1
    elif line[0] == "tgl":
        v = val(line[1])
        print(ip,v,toggle(ip+v-1))
print(reg["a"])

def f(x):
    if x is 2: return 2
    return x*f(x-1)

print(f(7) + 90*81)
print(f(12) + 90*81)
