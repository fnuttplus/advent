from sys import stdin
ins = stdin.read().splitlines()
ip = 0
reg = {}

def test(inst):
	r = inst[0]
	o = inst[1]
	i = int(inst[2])
	if r in reg: v = reg[r]
	else: v = 0
	if o == '>': return v > i
	elif o == '!=': return v != i
	elif o == '>=': return v >= i
	elif o == '<': return v < i
	elif o == '<=': return v <= i
	elif o == '==': return v == i
	else: print("error")
	
m = 0

while ip < len(ins):
	line = ins[ip].split()
	r,o,i = line[:3]
	i = int(i)
	if test(line[4:]):
		if line[1] == "inc":
			if r in reg: v = reg[r]
			else: v = 0
			reg[r] = v + i
			if m < reg[r]:
				m = reg[r]
		elif line[1] == "dec":
			if r in reg: v = reg[r]
			else: v = 0
			reg[r] = v - i
			if m < reg[r]:
				m = reg[r]
	ip += 1
print(max(reg.values()))
print(m)
