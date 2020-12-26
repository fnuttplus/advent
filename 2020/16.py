from sys import stdin

lines = [line.split("\n") for line in stdin.read().split("\n\n")]

d = {}
def isvalid(i):
    global d
    for dd in d:
        if d[dd][0] <= i <= d[dd][1] or d[dd][2] <= i <= d[dd][3]:
            return True
    return False

for line in lines[0]:
    if line == "": break
    l1 = line.split(": ")
    name = l1[0]
    a,b = line.split(": ")[1].split(" or ")
    a0, a1 = map(int, a.split("-"))
    b0, b1 = map(int, b.split("-"))
    d[name] = (a0, a1, b0, b1)

g = [[] for _ in range(20)]
n = 0
for line in lines[2][1:]:
    l = list(map(int, line.split(',')))
    for i in l:
        if not isvalid(i):
            n += i
            break
    else:
        for x in range(20):
            g[x].append(l[x])
print(n)

f = [[] for _ in range(20)]
for x in range(20):
    for dd in d:
        for gg in g[x]:
            if not (d[dd][0] <= gg <= d[dd][1] or d[dd][2] <= gg <= d[dd][3]):
                break
        else:
            f[x].append(dd)
    f[x] = (len(f[x]), x, set(f[x]))

s = set()
jj = []
for ff in sorted(f):
    if list(ff[2]-s)[0].startswith("departure"):
        jj.append(ff[1])
    #print(ff[1], list(ff[2]-s)[0])
    s |= (ff[2]-s)
#print(jj)
i = list(map(int, lines[1][1].split(",")))
p = 1
for j in jj:
    p *= i[j]
print(p)
