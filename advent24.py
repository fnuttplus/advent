from itertools import combinations as comb

def partition(s,w,n):
	for x in range(1,len(w)):
		for c in comb(w,x):
			if s == sum(c):
				if n > 1:
#					print(sorted(c), sum(c))
					return partition(s, w-set(c), n-1)
				else:
#					print(sorted(c), sum(c))
#					print(sorted(tuple(w-set(c))), sum(w-set(c)))
					return True
	return False

def solve(n):
	w = {1,2,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113}
	for x in range(1, len(w)):
		for c in comb(w, x):
			ww = w - set(c)
			sumc = sum(c)
			if sum(ww) == sumc*n:
				if partition(sumc, ww, n-1):
					qe = 1
					for p in c:
						qe*=p
#					print(sorted(c), sumc)
					return qe

print("Part 1:", solve(2))
print("Part 2:", solve(3))
#print(solve(4))
#print(solve(5))

#Part 1: 11846773891
#Part 2: 80393059
#[Finished in 1.6s]