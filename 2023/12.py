from sys import stdin
from re import findall
from aoc import Grid

def match(p, a):
    g = p.split('.')
    return [len(x) for x in g if len(x) > 0] == a

def perm(p, i = 0):
    if i+1 == len(p):
        if p[i] == '?':
            yield p[:-1] + ['.']
            yield p[:-1] + ['#']
        else:
            yield p
    else:
        if p[i] == '?':
            yield from perm(p[:i] + ['.'] + p[i+1:], i+1)
            yield from perm(p[:i] + ['#'] + p[i+1:], i+1)
        else:
            yield from perm(p, i+1)

memo = {}
def parse(pattern, eaten, groups):
    if (tuple(pattern), eaten, tuple(groups)) in memo:
        return memo[(tuple(pattern), eaten, tuple(groups))]
    if pattern == []:
        if len(groups) == 0 or (len(groups) == 1 and eaten == groups[0]):
            return 1
        return 0
    if pattern[0] == '?':
        m = parse(['#'] + pattern[1:], eaten, groups) + parse(['.'] + pattern[1:], eaten, groups)
        memo[(tuple(pattern), eaten, tuple(groups))] = m
        return m
    elif pattern[0] == '.':
        if eaten > 0:
            if len(groups) > 0 and eaten == groups[0]:
                return parse(pattern[1:], 0, groups[1:])
            return 0
        return parse(pattern[1:], 0, groups)
    elif pattern[0] == '#':
        if len(groups) == 0 or eaten + 1 > groups[0]:
            return 0
        if eaten == 0:
            return parse(pattern[1:], 1, groups)
        return parse(pattern[1:], eaten + 1, groups)

lines = stdin.read().splitlines()
s = 0
for line in lines:
    n = 0
    a,b = line.split(' ')
    a = a+'?'+a+'?'+a+'?'+a+'?'+a
    b = [int(x) for x in b.split(',')]
    b = 5*b
    n = parse(list(a), 0, b)
    #for p in perm(list(a)):
    #    if match(''.join(p), b):
    #        n += 1
    #print(n)
    s += n

print(s)
