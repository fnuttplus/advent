from sys import stdin
from aocd import get_data, submit
from re import findall

ls = stdin.read().splitlines()

def s(a):
    if a[1] > a[0]:
        for i in range(1, len(a)):
            if a[i] - a[i-1] < 1 or a[i] - a[i-1] > 3:
                return False
        else:
            return True
    if a[1] < a[0]:
        for i in range(1, len(a)):
            if a[i-1] - a[i] < 1 or a[i-1] - a[i] > 3:
                return False
        else:
            return True


c = 0
for l in ls:
    a = list(map(int, l.split(' ')))
    for i in range(len(a)):
        aa = a[:i] + a[i+1 :]
        if s(aa):
            c += 1
            break
print(c)