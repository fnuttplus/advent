from sys import stdin
from aocd import get_data, submit
from re import findall

ls = stdin.read().split('\n\n')
r = ls[0].split('\n')

s1 = 0
s2 = 0
for l in ls[1].split('\n'):
    ll = list(map(int,l.split(',')))
    yay = True
    for n in range(len(ll) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if f'{ll[i+1]}|{ll[i]}' in r:
                ll[i], ll[i + 1] = ll[i + 1], ll[i]
                swapped = True
                yay = False
        if not swapped:
            break
    if yay:
        s1 += ll[len(ll)//2]
    else:
        s2 += ll[len(ll)//2]

print(s1, s2)
