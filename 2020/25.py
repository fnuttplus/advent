from sys import stdin

c,d = map(int, stdin.read().splitlines())

n = 7

a = 1
i = 1
while True:
    i = (i * n) % 20201227
    if i == c: break
    a += 1
#print(a)
"""
b = 1
i = 1
while True:
    i = (i * n) % 20201227
    if i == d: break
    b += 1
print(b)
"""
i = 1
for _ in range(a):
    i = (i * d) % 20201227
print(i)
