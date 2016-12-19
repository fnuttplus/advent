print(int(bin(3001330)[3:]+'1',2))

w = 1
for x in range(2,3001330+1):
    if w >= x>>1: w += 1
    w += 1
    if w > x: w -= x
print(w)
