from sys import stdin
from dateutil.parser import parse


ids = [l.split(']') for l in stdin.read().splitlines()]
data = {}
for i in ids:
    d = parse(i[0][1:])
    data[d] = i[1].split()[1][1:]

m = 0
stat = {}
for k in sorted(data.keys()):
    if data[k] == "sleep":
        m = k.minute
    elif data[k] == "p":
        for x in range(m, k.minute):
            stat[g][x] += 1
    else:
        g = int(data[k])
        if not g in stat:
            stat[g] = {x: 0 for x in range(60)}

g = sorted(stat, key=lambda x: sum(stat[x].values()), reverse=True)[0]
print(g * max(stat[g], key=stat[g].get))

m = 0

for g in stat:
    for x in stat[g]:
        if stat[g][x] > m:
            m = stat[g][x]
            mx = x
            mg = g

print(m, mx, mg, mg*mx)