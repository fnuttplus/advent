print(int(bin(3001330)[3:]+'1',2))

def f(x):
    i = 1
    while i*3 < x: i*=3
    if x < 2*i: return x-i
    return 2*x-3*i

print(f(3001330))

w = 1
for x in range(2,3001330+1):
    if w >= x>>1: w += 1
    w += 1
    if w > x: w -= x
print(w)
