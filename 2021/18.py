from sys import stdin
from re import finditer, search

lines = stdin.read().splitlines()

def add(s, n, i=0):
    l = list(finditer(r"\d+", s))
    if l:
        s0,s1 = l[i].span()
        n = int(s[s0:s1]) + n
        return s[:s0] + str(n) + s[s1:]
    return s

def explode(s):
    d = 0
    for i in range(len(s)):
        c = s[i]
        if c == '[':
            if d==4:
                j = 1+s[i:].find(']')
                e = eval(s[i:i+j])
                return True, add(s[:i], e[0], -1) + '0' + add(s[i+j:], e[1])
            d += 1
        elif c == ']': d -= 1
    return False, s

def split(s):
    m = search(r"\d{2,}", s)
    if m:
        s0, s1 = m.span()
        i = int(s[s0:s1])
        a = b = i//2
        if i % 2 == 1: b += 1
        return True, f'{s[:s0]}[{a},{b}]{s[s1:]}'
    return False, s

def reduce(s):
    b = True
    while b:
        b, s = explode(s)
        while b:
            b, s = explode(s)
        b, s = split(s)
    return s

def magnitude(l):
    a,b = l
    if not isinstance(a, int): a = magnitude(a)
    if not isinstance(b, int): b = magnitude(b)
    return 3*a + 2*b

l = lines[0]
for line in lines[1:]:
    l = reduce(f'[{l},{line}]')
print(magnitude(eval(l)))

mm = 0
for a in lines:
    for b in lines:
        if a==b: continue
        m = magnitude(eval(reduce(f'[{a},{b}]')))
        if m > mm: mm = m
print(mm)
