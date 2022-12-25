from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

#ll = stdin.read().splitlines()
ll = get_data(day=25).splitlines()

c = 0
b = {'=':-2,'-':-1,'0':0,'1':1,'2':2,}

for l in ll:
    l = list(l)[::-1]
    s = 0
    for i in range(len(l)):
        s += 5**i*b[l[i]]
    c += s
print(c)
c = 36671616971741
i = 19
s = ''
while c != 0:
    a = c
    cca = '0'
    for cc in b:
        d = b[cc] * 5**i
        if abs(c-d) < abs(a):
            a = abs(c-d)
            cca = cc
            cd = d
    s += cca
    if a != c:
        c -= cd
    i -= 1
print(s)
