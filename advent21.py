from itertools import combinations as comb

"""
Player:
HP: 100

Boss:
Hit Points: 103
Damage: 9
Armor: 2

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armor = [(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
rings = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

def playerwins(damage, armor):
	playerHP = 100
	bossHP, bossD, bossA = 103, 9, 2
	turn = 1

	while True:
		if turn:
			bossHP -= (damage-bossA if damage-bossA > 1 else 1)
		else:
			playerHP -= (bossD-armor if bossD-armor > 1 else 1)
		if bossHP <= 0:
			return True
		if playerHP <= 0:
			return False
		turn = 0 if turn else 1

def calccost():
	cost = 0
	d = 0
	a = 0
	for g in gear:
		cost += g[0]
		d += g[1]
		a += g[2]
	return d,a,cost

for d in range(4,12):
	c = d+9
	for a in range(9):
		if playerwins(d,a):
			if c > a+d: c = a+d
#	print(d,c-d,c)

gear = {weapons[3], armor[1], rings[1]}
print(gear, calccost())

print("part 2")
for d in range(4,12):
	c = d
	for a in range(9):
		if not playerwins(d,a):
			if c < a+d: c = a+d
#	print(d,c-d,c)

gear = {weapons[0], armor[0], rings[2], rings[5]}
print(gear, calccost())

mincost = 1000
maxcost = 0
for w in weapons:
	gear = {w}
	for ai in range(len(armor)+1):
		if ai > 0:
			gear |= {armor[ai-1]}
		for r1i in range(len(rings)+1):
			if r1i > 0:
				gear |= {rings[r1i-1]}
			for r2i in range(r1i +1, len(rings)+1):
				gear |= {rings[r2i-1]}
				d,a,cost = calccost()
				if playerwins(d,a):
					if cost < mincost:
						mincost = cost
#						print("NEW LOW!", gear, cost)
				else:
					if cost > maxcost:
						maxcost = cost
#						print("NEW HIGH", gear, cost)
				gear -= {rings[r2i-1]}
			gear -= {rings[r1i-1]}
		gear -= {armor[ai-1]}

print("MIN:", mincost, "MAX:", maxcost)
