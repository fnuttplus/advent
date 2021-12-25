#from aocd import lines, submit
from sys import stdin

lines = stdin.read().splitlines()

h, d = 0,0
aim = 0
for l in lines:
    a,b = l.split(' ')
    b = int(b)
    if a == "forward":
        h += b
        d += aim * b
    if a == "down": aim += b
    if a == "up": aim -= b

print(h*d)
