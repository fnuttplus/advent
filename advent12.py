import json
o = json.loads(open("advent12.txt").read())

def gen(v):
	if isinstance(v, int):
		yield v
	elif isinstance(v, dict):
		red = False
		for k, d in v.items():
			if d == "red":
				red = True
		if red == False:
			for g in d_gen(v):
				yield g
	elif isinstance(v, list):
		for g in l_gen(v):
			yield g

def l_gen(l):
	for v in l:
		for g in gen(v):
			yield g

def d_gen(d):
	for k, v in d.items():
		for g in gen(v):
			yield g

s = 0
for i in d_gen(o):
	s += i

print(s)