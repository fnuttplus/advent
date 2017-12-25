from sys import stdin

g = stdin.read().splitlines()
y = 0
for i in range(len(g[0])):
	if g[0][i] is '|':
		x = i
d = [+1, 0]
found_end = False
s = ''
steps = 0
while True:
	n = g[y][x]
	if n is '+':
		if d[0] == 0:
			if not g[y+1][x] is ' ': d = [+1, 0]
			if not g[y-1][x] is ' ': d = [-1, 0]
		else:
			if not g[y][x+1] is ' ': d = [0, +1]
			if not g[y][x-1] is ' ': d = [0, -1]
	elif n in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		s += n
	elif n is ' ': break
	y += d[0]
	x += d[1]
	steps +=1

print(s, steps)