circuit = open("advent7.txt").read().split('\n')

for i in range(len(circuit)):
	circuit[i] = circuit[i].split()

memo = {}

def getsignal(wire):
	if wire in memo.keys():
		return memo[wire]
	for w in circuit:
		if w[-1] == wire:
#			print(w,memo)
			if len(w) == 3:
				if w[0].isdigit():
					memo[w[2]] = int(w[0])
					return int(w[0])
				else:
					r = getsignal(w[0])
					memo[w[2]] = r
					return r

			elif len(w) == 4:
				r = 65535-getsignal(w[1])
				memo[w[3]] = r
				return r
			elif len(w) == 5:
				if w[1] == 'OR':
					r = getsignal(w[0]) | getsignal(w[2])
				elif w[1] == 'LSHIFT':
					r = getsignal(w[0]) << int(w[2])
#					print(w,r,memo[w[0]])
				elif w[1] == 'RSHIFT':
					r = getsignal(w[0]) >> int(w[2])
				elif w[1] == 'AND':
					if w[0].isdigit():
						r = int(w[0]) & getsignal(w[2])
					else:
						r = getsignal(w[0]) & getsignal(w[2])
				memo[w[4]] = r
				return r

#	print("FALL THROUGH")
#	return 0

print(getsignal('a'))

#for s in memo.keys():
#	if memo[s] > 65535:
#		print(s,memo[s])
