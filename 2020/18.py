from sys import stdin

def lastp(l, j):
    n = 0
    for i in range(j+1, len(l)):
        if l[i] == '(': n += 1
        elif l[i] == ')':
            if n == 0: return i
            else: n -= 1

def parse(l):
    op, i, n = '', 0, 0
    while i < len(l):
        c = l[i]
        if c == '*' or c == '+':
            op = c
        elif c == '(':
            c = parse(l[i+1:lastp(l, i)])
            i = lastp(l, i)
            if op == '+': n += c
            elif op == '*': n *= c
            else: n = c
        else:
            if op == '+': n += int(c)
            elif op == '*': n *= int(c)
            else: n = int(c)
        i += 1
    return n

n = 0
for line in stdin.read().splitlines():
    #print(line)
    p = parse(list(line.replace(' ', '')))
    #print(p)
    n += p
print(n)
