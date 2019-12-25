from sys import stdin
import math

a = list(map(int, stdin.read().splitlines()))
n = 0
for aa in a:
    m = math.floor(aa/3)-2
    while m >0:
        n += m
        m = math.floor(m/3)-2
print(n)
