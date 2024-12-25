from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations

s = 0

r = {}

t = True
t = False

ls = stdin.read() if t else get_data()
ls = list(map(int, list(ls)))

dd = []
i = 0
f = True
ff = {}
fs = []
for c in ls:
    if f:
        ff[i] = (len(dd), c)
        dd += [i] * c
        i += 1
    else:
        fs.append((len(dd), c))
        dd += [-1] * c
    f = not f

if t: print(ff, fs, i)

for j in range(i-1, 0, -1):
    for k in range(len(fs)):
        a,b = fs[k]
        if a >= ff[j][0]: break
        if b >= ff[j][1]:
            for l in range(a, a+ff[j][1]):
                dd[l] = j
            for l in range(ff[j][0], ff[j][0]+ff[j][1]):
                dd[l] = -1
            fs[k] = (a+ff[j][1], b-ff[j][1])
            break
    if t: print(dd)

for i in range(len(dd)):
    if dd[i] != -1:
        s += i * dd[i]

if t:
    print(s)
else:
    print(s)
