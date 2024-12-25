from sys import stdin
from aocd import get_data, submit
from re import findall

ls = stdin.read().splitlines()
l1 = []
l2 = []

for l in ls:
    a, b = map(int, l.split('   '))
    l1.append(a)
    l2.append(b)

l1.sort()
l2.sort()

d = 0
for i in range(len(l1)):
    a = l1[i]
    b = l2[i]

    #d += abs(a-b)
    d += a * l2.count(a)

print(d)