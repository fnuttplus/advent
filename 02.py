from sys import stdin

r = {2:3,3:4,5:6,6:7,7:8,8:9,'A':'B','B':'C',}
l = {r[k]:k for k in r}
d = {2:6,6:'A',1:3,3:7,7:'B','B':'D',4:8,8:'C',}
u = {d[k]:k for k in d}

k = 5
for line in stdin:
	for c in line:
		if c is 'U':
			if k in u: k = u[k]
#			if k > 3: k -= 3
		elif c is 'D':
			if k in d: k = d[k]
#			if k < 7: k += 3
		elif c is 'L':
			if k in l: k = l[k]
#			if k%3 != 1: k -= 1
		elif c is 'R':
			if k in r: k = r[k]
#			if k%3 != 0: k += 1
	print(k,end='')
