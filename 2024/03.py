from sys import stdin
from aocd import get_data, submit
from re import findall

ls = stdin.read().splitlines()

s = 0
do = True
for l in ls:
    c = findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)', l)
    for cc in c:
        if cc == 'do()':
            do = True
        elif cc == 'don\'t()':
            do = False
        else:
            a,b = map(int, findall('\d+', cc))
            if do:
                s += a*b

print(s)