from sys import stdin
from aocd import submit, get_data, lines

#for line in stdin.read().splitlines():

s = get_data(day=6)
#s = input()
n = 14
for i in range(n, len(s)):
    if len(set(s[i-n:i])) == n:
        print(i)
        break
