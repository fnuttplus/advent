instructions = open("advent23.txt").read().split('\n')

ip = 0
reg = {'a':0, 'b':0}

while ip < len(instructions):
	ins = instructions[ip].split()
	r = ins[1][0]
#	if r not in reg.keys():	reg[r] = 0
	print(ip+1,repr(ins).ljust(20),reg)
	if ins[0] == "hlf":
		reg[r]//= 2
	elif ins[0] == "tpl":
		reg[r] *= 3
	elif ins[0] == "inc":
		reg[r] += 1
	elif ins[0] == "jmp":
		ip = ip + int(ins[1][1:])*(-1 if r == '-' else 1) -1
	elif ins[0] == "jie":
		if reg[r]%2 == 0:
			ip = ip + int(ins[2][1:])*(-1 if ins[2][0] == '-' else 1) -1
	elif ins[0] == "jio":
		if reg[r] == 1:
			ip = ip + int(ins[2][1:])*(-1 if ins[2][0] == '-' else 1) -1
	ip += 1

print(reg['b'])