from vm import Computer
ins = input()

def get(x, y):
    comp = Computer(ins, False)
    comp.start()
    comp.inq.put(x)
    comp.inq.put(y)
    return comp.outq.get()

for x in range(950, 1000):
    for y in range(475, 500):
        if get(x+99,y) == 1 and get(x,y+99) == 1:
            print(x*10000+y)
            break
    else: continue
    break

i = 0
for y in range(50):
    for x in range(50):
        q = get(x,y)
        i += q
        print("#" if q == 1 else ".", end="")
    print()
print(i)