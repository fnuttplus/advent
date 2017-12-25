from sys import stdin

ins = [l.split() for l in stdin.read().splitlines()]

def val(v):
	if v in reg[pid]: return reg[pid][v]
	return int(v)

pid = 0
ip = [0, 0]
reg = [{a: 0 for a in 'abcdefghijklmnopqrstuvwxyz'},{a: 0 for a in 'abcdefghijklmnopqrstuvwxyz'}]
reg[1]['p'] = 1

snd = [[],[]]

count = 0
while ip[pid] < len(ins):
	i = ins[ip[pid]]
	ip[pid] += 1
	if   i[0] == "snd":
		if pid == 1:
			count += 1
		snd[pid].append(val(i[1]))
	elif i[0] == "set": reg[pid][i[1]] = val(i[2])
	elif i[0] == "add": reg[pid][i[1]] += val(i[2])
	elif i[0] == "mul": reg[pid][i[1]] *= val(i[2])
	elif i[0] == "mod": reg[pid][i[1]] %= val(i[2])
	elif i[0] == "jgz":
		if val(i[1]) > 0: ip[pid] += val(i[2])-1
	elif i[0] == "rcv":
		rcv = 1 if pid == 0 else 0
		if len(snd[rcv]) > 0:
			reg[pid][i[1]] = snd[rcv].pop(0)
		else:
			if len(snd[pid]) == 0: break
			pid = 1 if pid == 0 else 0
			ip[pid] -= 1
print(count)