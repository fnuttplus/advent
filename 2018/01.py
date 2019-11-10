from sys import stdin
fa = [0]
f = 0
ins = [int(l) for l in stdin.read().splitlines()]
print(sum(ins))
for i in ins:
    f += i
    fa.append(f)
#-55310 +137*406 = 312
m = 1
while True:
    for i in range(len(fa)):
        if m * fa[-1] + fa[i] in fa[:i]:
            print(m * fa[-1] + fa[i])
            raise SystemExit
    m += 1
