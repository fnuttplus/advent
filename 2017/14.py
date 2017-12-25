knot_hash = __import__('10').knot_hash


g = [['#' if d=='1' else '.' for d in list(bin(int(knot_hash("hxtvlmkl-"+str(i)), 16))[2:].zfill(128))] for i in range(128)]
i = 0
for row in g:
	i += row.count('#')
print(i)

def fill(x,y,i):
	g[y][x] = str(i)
	for dx,dy in [(0,1),(1,0),(-1,0),(0,-1),]:
		if x+dx >= 0 and x+dx < len(g[y]) and y+dy >= 0 and y+dy < len(g):
			if g[y+dy][x+dx] is '#':
				fill(x+dx, y+dy, i)

#print('\n'.join([''.join(row) for row in g]))
i = 1
for y in range(len(g)):
	for x in range(len(g[y])):
		if g[y][x] is '#':
			fill(x,y,i)
			i += 1

print(i-1)