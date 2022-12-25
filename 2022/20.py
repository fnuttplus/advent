from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

ll = stdin.read().splitlines()
ll = get_data(day=20).splitlines()

ll = list(map(int, ll))
ll = [x*811589153 for x in ll]
l = [(i,e) for i,e in enumerate(ll)]
for _ in range(10):
    for i, e in enumerate(ll):
        j = l.index((i,e))
        l.remove((i,e))
        l.insert((j + e) % len(l), (i,e))
#    print(l)
i = 0
for _,e in l:
    if e == 0:
        break
    i += 1
print(l[(i+1000)%len(l)][1] + l[(i+2000)%len(l)][1] + l[(i+3000)%len(l)][1])
