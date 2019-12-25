from itertools import permutations
import threading
from vm import Computer

print("Running...")

for x in range (100):
    for y in range(100):
        comp = Computer(open("advent/02.in").read())
        comp.ins[1] = x
        comp.ins[2] = y
        comp.run()
        if comp.ins[0] == 19690720:
            print("day 02:", 100*x+y)
print("       ", 6979)

comp = Computer(open("advent/05.in").read())
comp.inq.put(5)
comp.run()
print("day 05:", next(comp.get()))
print("       ", 3629692)

ins = open("advent/07.in").read()
m = 0
for p in permutations([5,6,7,8,9], 5):
    comp = [Computer(ins) for _ in range(5)]
    for i in range(5):
        comp[i].start()
        comp[i].inq.put(p[i])
    comp[0].inq.put(0)
    i = 0
    while True:
        r = comp[i].outq.get()
        i = (i + 1) % 5
        comp[i].inq.put(r)
        if r is None:
            if x > m: m = x
            break
        x = r
print("day 07:", m)
print("       ", 19539216)

comp = Computer(open("advent/09.in").read())
comp.inq.put(2)
comp.run()
print("day 09:", next(comp.get()))
print("       ", 84513)
