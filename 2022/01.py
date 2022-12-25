from sys import stdin
from aocd import get_data, submit

a = []
for elf in get_data(day=1).split('\n\n'):
    s = sum(list(map(int, elf.split('\n'))))
    a.append(s)
print(sum(sorted(a,reverse=True)[:3]))