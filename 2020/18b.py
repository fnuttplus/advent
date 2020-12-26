from sys import stdin

def term():
    global i
    a = exp() if peek('(') else int(l[i])
    i += 1
    return a

def peek(c):
    global i
    if i < len(l) and l[i] == c:
        i += 1
        return True
    return False

def summa():
    a = term()
    while peek('+'): a += term()
    return a

def exp():
    a = summa()
    while peek('*'): a *= summa()
    return a

n = 0
for line in stdin.read().splitlines():
    l = list(line.replace(' ', ''))
    i = 0
    n += exp()
print(n)
