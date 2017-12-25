from sys import stdin

lines = stdin.read().splitlines()
graph = {}
for line in lines:
	g = line.split(' ')
	g = [int(g[0])] + [int(g[-1])] + list(map(int, [l[:-1] for l in g[2:-1]]))
	graph[g[0]] = g[1:]

s = [0]
visited = set([0])

while s:
	ns = set()
	for root in s:
		visited.add(root)
		for node in graph[root]:
			if node not in visited:
				ns.add(node)
	s = ns
print(len(visited))

groups = [[i] for i in range(2000)]

def find(root):
	global groups
	for i in range(len(groups)):
		if root in groups[i]:
			return i

i = 0
while i < len(groups):
	s = groups[i]
	while s:
		ns = set()
		for root in s:
			for node in graph[root]:
				if node not in groups[i]:
					groups[i] += groups.pop(find(node))
					ns.add(node)
		s = ns
	i += 1
print(len(groups))
	

