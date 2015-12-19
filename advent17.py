s = 0

def combinations(m, con, used):
	n = 0
	for i in range(len(con)):
		if con[i] < m:
			if i < len(con)-1:
				n += combinations(m-con[i], con[i+1:], used + [con[i]])
		elif con[i] == m:
			if len(used) < 4:
				global s
				s += 1
#				print(len(used)+1, used+[con[i]], s)
			n += 1
	return n

#ctest = [20,15,10,5,5]
containers = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]

print(combinations(150, containers, []), s)
#print(combinations(25, ctest, []))
