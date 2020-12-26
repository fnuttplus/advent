from sys import stdin

l = []
e = set()
for line in stdin.read().splitlines():
    a,b = line.split(" (contains ")
    b = b[:-1].split(", ")
    a = a.split(' ')
    l.append([set(a),set(b)])
    e |= set(b)

for ee in e:
    a = set()
    for ll in l:
        if ee in ll[1]:
            if a == set():
                a = ll[0]
            else:
                a = a & ll[0]
    print(ee, ','.join(a))

solved = set("vrzkz,zjsh,hphcb,mbdksj,vzzxl,ctmzsr,rkzqs,zmhnj".split(','))

n = 0
for ll in l:
    n += len(ll[0] - solved)
print(n)

"""
dairy vrzkz
eggs zjsh
fish hphcb
nuts mbdksj
peanuts vzzxl
sesame ctmzsr
shellfish rkzqs
soy zmhnj
"""