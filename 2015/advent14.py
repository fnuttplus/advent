reindeers = [
{"name": "Vixen", "v": 19, "t": 7, "rest": 124},
{"name": "Rudolph", "v": 3, "t": 15, "rest": 28},
{"name": "Donner", "v": 19, "t": 9, "rest": 164},
{"name": "Blitzen", "v": 19, "t": 9, "rest": 158},
{"name": "Comet", "v": 13, "t": 7, "rest": 82},
{"name": "Cupid", "v": 25, "t": 6, "rest": 145},
{"name": "Dasher", "v": 14, "t": 3, "rest": 38},
{"name": "Dancer", "v": 3, "t": 16, "rest": 37},
{"name": "Prancer", "v": 25, "t": 6, "rest": 143}]



def get_leaders(goal):
	l = []
	d = 0
	for r in reindeers:
#		print(r["name"], "can fly", r["v"], "km/s for", r["t"], "seconds, but then must rest for", r["rest"], "seconds.")
		mod = goal%(r["rest"]+r["t"])
		distance = (goal//(r["rest"]+r["t"])) * r["v"]*r["t"] + r["v"]*(mod if (mod < r["t"]) else r["t"])
		if distance == d:
			l.append(r["name"])
		elif distance > d:
			l = [r["name"]]
			d = distance

#		print("It has travelled", distance, "km.")
	return l

points = {"Vixen": 0, "Rudolph": 0, "Donner": 0, "Blitzen": 0, "Comet": 0, "Cupid": 0, "Dasher": 0, "Dancer": 0, "Prancer": 0}

for d in range(2503):
	leaders = get_leaders(d+1)
	for l in leaders:
		points[l] += 1
#	print(d+1, get_leaders(d+1))
print(points)
