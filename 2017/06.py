from sys import stdin

def redis(l):
	m = 0
	mi = 0
	for i in range(len(l)):
		if l[i] > m:
			m = l[i]
			mi =  i
	k = m//len(l)
	l[mi] = 0
	for _ in range(m % len(l)):
		mi += 1
		if mi == len(l):
			mi = 0
		l[mi] += k + 1
	for _ in range(len(l) - (m % len(l))):
		mi += 1
		if mi == len(l):
			mi = 0
		l[mi] += k


l = list(map(int,stdin.read().split('\t')))
seen = []
i = 0
while tuple(l) not in seen:
	seen.append(tuple(l))
	redis(l)
	i += 1
print(i-seen.index(tuple(l)))
