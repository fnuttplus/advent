#using cude coordinates
#https://www.redblobgames.com/grids/hexagons/
def move(x,y,z,d):
	if d == 'n':
		return x, y+1, z-1
	elif d == 'nw':
		return x-1, y+1, z
	elif d == 'ne':
		return x+1, y, z-1
	elif d == 's':
		return x, y-1, z+1
	elif d == 'sw':
		return x-1, y, z+1
	elif d == 'se':
		return x+1, y-1, z

def dist(x,y,z):
	return max(map(abs, [x,y,z]))

x,y,z = 0,0,0
moves = input().split(',')
md = 0
for m in moves:
	x,y,z = move(x,y,z,m)
	d = dist(x,y,z)
	if d > md:
		md = d

print(x,y,z)
print(dist(x,y,z),md)
