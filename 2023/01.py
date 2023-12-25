from sys import stdin
from aocd import get_data, submit
from re import findall

s = 0
for line in stdin.read().splitlines():
    a = []
    b = findall('(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    print(line)
    print(b)
    for m in b:
        if m == "one": a.append('1')
        elif m == 'two': a.append('2')
        elif m == 'three': a.append('3')
        elif m == 'four': a.append('4')
        elif m == 'five': a.append('5')
        elif m == 'six': a.append('6')
        elif m == 'seven': a.append('7')
        elif m == 'eight': a.append('8')
        elif m == 'nine': a.append('9')
        else: a.append(m)
    print(a)
    print(int(a[0] + a[-1]))
    s += int(a[0] + a[-1])

print(s)