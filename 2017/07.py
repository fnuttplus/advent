from sys import stdin

data = stdin.read().splitlines()

discs = {}

for row in data:
	row = row.split()
	discs[row[0]] = [int(row[1][1:-1]), []]
	if len(row) > 2:
		discs[row[0]][1] = [disc[:-1] for disc in row[3:-1]] + [row[-1]]
	print(row)

root = 'rugzyaj'


def weight(root):
	w = discs[root][0]
	for branch in discs[root][1]:
		w += weight(branch)
	return w

for branch in discs[root][1]:
	print(branch, weight(branch))

print(weight(root))
