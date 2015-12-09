from itertools import permutations as perm

dist = [
("Faerun", "Tristram", 65),
("Faerun", "Tambi", 129),
("Faerun", "Norrath", 144),
("Faerun", "Snowdin", 71),
("Faerun", "Straylight", 137),
("Faerun", "AlphaCentauri", 3),
("Faerun", "Arbre", 149),
("Tristram", "Tambi", 63),
("Tristram", "Norrath", 4),
("Tristram", "Snowdin", 105),
("Tristram", "Straylight", 125),
("Tristram", "AlphaCentauri", 55),
("Tristram", "Arbre", 14),
("Tambi", "Norrath", 68),
("Tambi", "Snowdin", 52),
("Tambi", "Straylight", 65),
("Tambi", "AlphaCentauri", 22),
("Tambi", "Arbre", 143),
("Norrath", "Snowdin", 8),
("Norrath", "Straylight", 23),
("Norrath", "AlphaCentauri", 136),
("Norrath", "Arbre", 115),
("Snowdin", "Straylight", 101),
("Snowdin", "AlphaCentauri", 84),
("Snowdin", "Arbre", 96),
("Straylight", "AlphaCentauri", 107),
("Straylight", "Arbre", 14),
("AlphaCentauri", "Arbre", 46)]

towns = ["Faerun", "Tristram", "Tambi", "Norrath", "Snowdin", "Straylight", "AlphaCentauri", "Arbre"]

def getdist(town1, town2):
	for d in dist:
		if (d[0] == town1 and d[1] == town2) or (d[1] == town1 and d[0] == town2):
			return d[2]

maxd = 0
#brute force 40320 permutations
for p in perm(range(8),8):
	d = 0
	town1 = p[0]
	for town2 in p[1:]:
		d += getdist(towns[town1], towns[town2])
		town1 = town2
	if d > maxd:
		for town in p:
			print(towns[town], end=" -> ")
		maxd = d
		print(d)

print(maxd)

