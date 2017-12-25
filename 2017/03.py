g = [[0 for _ in range(1000)] for _ in range(1000)]

x,y=0,0
i = 1
g[y][x] = i

a = 2

while i < 277678:
	x += 1
	y -= 1
	for dx,dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
		for _ in range(a):
			x += dx
			y += dy
			i += 1
			#i = sum([g[y][x-1], g[y][x+1], g[y-1][x], g[y+1][x], g[y-1][x-1], g[y+1][x+1], g[y-1][x+1], g[y+1][x-1]])
			if i == 277678: print(x,y,i,abs(y)+abs(x))
			g[y][x] = i
	a += 2

for y in range(10, -10, -1):
	for x in range(-10, 10):
		print(str(g[y][x]).center(3), end=' ')
	print()
