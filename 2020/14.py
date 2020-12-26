from sys import stdin

def maskify(b) :
    return bin(int(b))[2:].zfill(36)

def xor(m, b):
    x = ""
    for i in range(len(m)):
        if m[i] == "X":
            x += b[i]
        else:
            x += m[i]
    return int(x, 2)

def ab(m, b, c):
    i = 0
    x = ""
    b = bin(int(b))[2:].zfill(c)
    for j in range(len(m)):
        if m[j] == "X":
            x += b[i]
            i += 1
        else:
            x += m[j]
    return int(x, 2)

def addr(m, b):
    x = ""
    for i in range(len(m)):
        if m[i] == "0":
            x += b[i]
        else:
            x += m[i]
    for i in range(2**x.count("X")):
        yield ab(x, i, x.count("X"))

mem1 = {}
mem2 = {}
for line in stdin.read().splitlines():
    a, b = line.split(" = ")
    if a == "mask": mask = b
    else: 
        i = int(a.split('[')[1][:-1])
        mem1[i] = xor(mask, maskify(b))
        for i in addr(mask, maskify(i)):
            mem2[i] = int(b)

print(sum([mem1[i] for i in mem1]))
print(sum([mem2[i] for i in mem2]))
