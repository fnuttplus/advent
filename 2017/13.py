from sys import stdin

lines = stdin.read().splitlines()
firewall = {}
for l in lines:
	a,b = map(int, l.split(': '))
	firewall[a] = 2*(b-1)

caught = True
i = 0
x = 0
while caught:
	caught = False
	for wall in firewall:
		if (wall + i) % firewall[wall] == 0:
			caught = True
			break
			#x += (firewall[wall]//2+1) * wall
	i += 1

print(i-1)
