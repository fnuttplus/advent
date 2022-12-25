from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image
from functools import cmp_to_key

ll = stdin.read().split('\n\n')
ll = get_data(day=13).split('\n\n')
i = 1
s = []

def compare(a,b):
    #print(a,b)
    if not isinstance(a, list) and not isinstance(b, list):
        if a < b: return 1
        if a > b: return -1
        if a == b: return 0

    if not isinstance(a, list): a = [a]
    if not isinstance(b, list): b = [b]

    for j in range(len(a)):
        #print('j', j)
        if j == len(b):
            return -1
        c = compare(a[j], b[j])
        if c == 0: continue
        return c
    else:
        if len(a) == len(b): return 0
        return 1

al = []
for l in ll:
    a,b = l.split('\n')
    a = eval(a)
    b = eval(b)
    al.append(a)
    al.append(b)
    print(a,b)
    #print(compare(a,b))
    #if compare(a,b) == 1: s.append(i)
    #i += 1
al.append([[2]])
al.append([[6]])
#print(al)

al.sort(key=cmp_to_key(compare),reverse=True)
print(al.index([[2]])+1)
print(al.index([[6]])+1)
#print(al)
print((al.index([[2]])+1) * (al.index([[6]])+1))
