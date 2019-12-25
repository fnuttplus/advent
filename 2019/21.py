from vm import Computer

comp = Computer(input(), False)
comp.start()
for c in """NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
""": comp.inq.put(ord(c))

while True:
    q = comp.outq.get()
    if q is None: break
    if q > 255: print(q)
    else: print(chr(q),end="")

#!A or !B or !C and D and (E or H)