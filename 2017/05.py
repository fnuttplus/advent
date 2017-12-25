from sys import stdin

l = list(map(int,stdin.read().splitlines()))

i,j = 0,0

while i >= 0 and i < len(l):
	t = i
	i += l[i]
	if l[t] >= 3: l[t] -= 1
	else: l[t] += 1
	j += 1

print(i,j)
