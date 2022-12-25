from sys import stdin
from aocd import get_data, submit

s = 0
"""
for l in stdin.read().splitlines():
    a,b = l[:len(l)//2],l[len(l)//2:]
    a = set(list(a))
    b = set(list(b))
    ss = list(a & b)
    s += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(ss[0])+1
"""
l = get_data(day=3).splitlines()

for i in range(0,len(l),3):
    a = set(list(l[i]))
    b = set(list(l[i+1]))
    c = set(list(l[i+2]))
    ss = list(a & b & c)
    s += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(ss[0])+1

print(s)
