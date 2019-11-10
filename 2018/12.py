from sys import stdin

pi = stdin.read().splitlines()
d = {}
s = ['.'] * 256

ss = pi[0].split()[2]
for i in range(len(ss)):
    s[i+10] = ss[i]

for p in pi[2:]:
    k,_,v = p.split()
    d[k] = v

print(6505+34*(50000000000-191))

for g in range(200):
    ns = ['.'] * 256
    for i in range(3, 250):
        ns[i] = d[''.join(s[i-2:i+3])]
    s = ns
    print(''.join(s))
    n = 0
    for i in range(len(s)):
        if s[i] == "#":
            n += i-10
#    print(g, n, 6505+34*(g-190))
#    print(''.join(s).count("#"))
