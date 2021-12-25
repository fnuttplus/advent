from sys import stdin

lines = stdin.read().splitlines()

p = [4,2]
s = [0,0]

di = 0
def roll():
    global di
    di += 1
    return (di-1) % 100 + 1

i = 0
while True:
    d = sum(roll() for _ in range(3))
    p[i] = (p[i] + d) % 10
    s[i] += 10 if p[i] == 0 else p[i]
    if s[i] >= 1000: break
    i = 1 if i == 0 else 0

print(min(s)*di)
