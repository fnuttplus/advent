a,b = 1,1
for _ in range(26+7): a,b = a+b,a
print(a+14*14)

from sys import stdin
ins = stdin.read().splitlines()
ip = 0
reg = {a:0 for a in "abcd"}
reg["c"] = 1
while ip < len(ins):
    line = ins[ip].split()
    ip += 1
    if line[0] == "cpy":
        if line[1] in reg: v = reg[line[1]]
        else: v = int(line[1])
        reg[line[2]] = v
    elif line[0] == "inc":
        reg[line[1]] += 1        
    elif line[0] == "dec":
        reg[line[1]] -= 1        
    elif line[0] == "jnz":
        if line[1] in reg: v = reg[line[1]]
        else: v = int(line[1])
        if v: ip += int(line[2])-1
print(reg["a"])
