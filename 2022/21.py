from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

ll = stdin.read().splitlines()
ll = get_data(day=21).splitlines()

d = {}
for l in ll:
    s = l.split(' ')
    if len(s) == 2:
        d[s[0][:-1]] = int(s[1])
    else:
        a, b,op,c = s
        a = a[:-1]
        d[a] = (b,op,c)

def rec(p):
    if type(d[p]) == int:
        if p == 'humn': return d[p], 'x'
        return d[p], str(d[p])
    a,op,b = d[p]
    a = rec(a)
    b = rec(b)
    sa = a[1]
    sb = b[1]
    a = a[0]
    b = b[0]
    if p == 'root': return f'{sa}=={sb}'
    if op == '+': return a+b, f'({sa}+{sb})'
    if op == '-': return a-b, f'({sa}-{sb})'
    if op == '*': return a*b, f'({sa}*{sb})'
    if op == '/': return a/b, f'({sa}/{sb})'

print(rec('root'))
