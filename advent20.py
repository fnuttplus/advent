#part 2:
s = [0] * 10**6
i = 10000
while True:
	for x in range(1,51):
		if i*x >= 10**6: break
		s[i*x] += i*11
	if s[i] > 29000000: break
	i+=1
print(i, s[i])

#part 1:
n = 0
i = 650000
while n < 2900000:
	i += 2
	n = i+1
	d = 2
	while d*d < i:
		if i % d == 0:
			n += (i//d) + d
		d+=1
	if d*d == i: n += d
print(i,n*10)

#705600 29002446
#665280 29260800
#[Finished in 8.4s]