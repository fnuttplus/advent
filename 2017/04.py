from sys import stdin

s = [row.split() for row  in stdin.read().splitlines()]
print(s)

i = 0

for row in s:
	row = [''.join(sorted(list(word))) for word in row]
	if len(row) == len(set(row)):
		i += 1
print(i)