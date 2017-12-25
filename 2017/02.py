from sys import stdin

s = [list(map(int, row.split("\t"))) for row  in stdin.read().splitlines()]

i = 0
for row in s:
	for a in row:
		for b in row:
			if a > b and a % b == 0:
				i += a//b
#	i += max(row) - min(row)

print(i)
