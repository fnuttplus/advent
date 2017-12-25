program = [a for a in 'abcdefghijklmnop']

recording = input().split(',')
for i in range(1, 1000000000 % 60):
	for dance_move in recording:
		dm = dance_move[0]
		if dm is 's':
			i = int(dance_move[1:])
			program = program[-i:] + program[:-i]
		elif dm is 'x':
			a,b = map(int, dance_move[1:].split('/'))
			program[a], program[b] = program[b], program[a]
		elif dm is 'p':
			a,b = map(program.index, dance_move[1:].split('/'))
			program[a], program[b] = program[b], program[a]
	if ''.join(program) == 'abcdefghijklmnop':
		print(i)
		break
print(''.join(program))
