from sys import stdin
from aocd import submit, get_data, lines
"""
[T] [V]                     [W]
[V] [C] [P] [D]             [B]
[J] [P] [R] [N] [B]         [Z]
[W] [Q] [D] [M] [T]     [L] [T]
[N] [J] [H] [B] [P] [T] [P] [L]
[R] [D] [F] [P] [R] [P] [R] [S] [G]
[M] [W] [J] [R] [V] [B] [J] [C] [S]
[S] [B] [B] [F] [H] [C] [B] [N] [L]
 1   2   3   4   5   6   7   8   9
"""
stacks = [
    list('SMRNWJVT'),
    list('BWDJQPCV'),
    list('BJFHDRP'),
    list('FRPBMND'),
    list('HVRPTB'),
    list('CBPT'),
    list('BJRPL'),
    list('NCSLTZBW'),
    list('LSG'),
]

#for line in stdin.read().splitlines():
for line in lines[10:]:
    a = int(line.split(' ')[1])
    b = int(line.split(' ')[3])
    c = int(line.split(' ')[5])
    #for _ in range(a): stacks[c-1].append(stacks[b-1].pop())
    stacks[c-1] += stacks[b-1][-a:]
    stacks[b-1] = stacks[b-1][:-a]
    #print(stacks)

print(''.join([s[-1] for s in stacks]))
