from sys import stdin

g = [[set(list(y)) for y in x.split('\n')] for x in stdin.read().split('\n\n')]

print(sum([len(set.union(*gg)) for gg in g]))
print(sum([len(set.intersection(*gg)) for gg in g]))
