from re import search
from operator import lt, gt, eq

facts = [
	["children", 3, eq],
	["cats", 7, gt],
	["samoyeds", 2, eq],
	["pomeranians", 3, lt],
	["akitas", 0, eq],
	["vizslas", 0, eq],
	["goldfish", 5, lt],
	["trees", 3, gt],
	["cars", 2, eq],
	["perfumes", 1, eq]]

for line in open("advent16.txt").readlines():
	match = True
	for fact in facts:
		rem = search(fact[0] +": (\d+)", line)
		if rem:
			var = int(rem.group(1))
			if not fact[2](var, fact[1]):
				match = False

	if match: print(line)