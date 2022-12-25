from sys import stdin
import re
from aocd import get_data, submit

s = 0

for line in get_data(day=4).splitlines():
    #a,b = line.split(',')
    #a1,a2 = map(int, a.split('-'))
    #b1,b2 = map(int, b.split('-'))
    #if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
    a1,a2,b1,b2 = map(int, re.split('-|,', line))
    if a1 <= b2 and b1 <= a2:
        s += 1
print(s)
