#buffer = [0]

i = 0
x = 1
for n in range(1, 50002018):
	i = (i + 328) % x + 1
	x += 1
	if i == 1: print(n)
	#buffer.insert(i,n)
#print(buffer[i+1])
