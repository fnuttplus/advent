def move(l,dx,dy):
	global x,y
	for _ in range(1, l+1):
		y += dy
		x += dx
		if (x,y) in memo: return True
		else: memo.add((x,y))
	return False
memo = set()

s = input().split(", ")
x,y = 0,0
d = 0 #north
for ss in s:
	t = ss[0]
	l = int(ss[1:])
	tl = t is 'L'
	if   d is 0: d = 1 if tl else 2
	elif d is 1: d = 3 if tl else 0
	elif d is 2: d = 0 if tl else 3
	elif d is 3: d = 2 if tl else 1

	if d is 0:
#		y += l
		if move(l,0,1): break
	elif d is 1:
#		x += l
		if move(l,1,0): break
	elif d is 2:
#		x -= l
		if move(l,-1,0): break
	elif d is 3:
#		y -= l
		if move(l,0,-1): break

#	print(t,l)
#	print(x,y,d)
print(abs(x) + abs(y))
