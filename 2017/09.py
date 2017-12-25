i = 0
g = 0
garbage = False
ignore = False
j = 0
for s in input():
	if ignore:
		ignore = False
	elif s is '!':
		ignore = True
	elif garbage:
		if s is '>':
			garbage = False
		else: j += 1
	elif s is '{':
		g += 1
	elif s is '}':
		i += g
		g -= 1
	elif s is '<':
		garbage = True


print(i,j)