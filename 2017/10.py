def knot_hash(string):
	l = [i for i in range(256)]
	p = 0
	s = 0
	lengths = list(map(ord, string)) + [17, 31, 73, 47, 23]
	def rev(p, le):
		nonlocal l
		nl = l[p:p+le]
		if p+le > len(l):
			nl += l[0:p+le-len(l)]
			nl = list(reversed(nl))
			l = nl[len(l)-p:] + l[len(nl)-len(l)+p:-len(l)+p] + nl[:len(l)-p]
		else:
			nl = list(reversed(nl))
			l = l[:p] + nl + l[p+le:]
		return l

	for _ in range(64):
		for length in lengths:
			rev(p, length)
			p += length + s
			p %= 256
			s += 1

	h = [0 for _ in range(16)]
	hash = ''
	for j in range(16):
		for i in range(16):
			h[j] ^= l[j*16+i]
		hash += hex(h[j])[2:].zfill(2)
	return hash

print(knot_hash(input()))
