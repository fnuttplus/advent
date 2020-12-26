from sys import stdin

l = list(map(int, list("962713854")))# + list(range(10,1001))
m = 1000000
il = [0 for _ in range(m+1)]
il[-1] = l[0]
for i in range(1, len(l)):
    il[l[i-1]] = l[i]
il[l[-1]] = 10
#il[l[-1]] = l[0]
for i in range(10, m): il[i] = i+1
#print(il)

d = l[0]
for x in range(m*10):
    a = il[d]
    b = il[a]
    c = il[b]
    il[d] = il[c]
    i = d-1
    if i == 0: i = m
    while i in [a,b,c]:
        i -= 1
        if i == 0: i = m
    il[c] = il[i]
    il[i] = a
    d = il[d]
    if x % m == 0:
        print(x//m, il[1], il[il[1]])

print(il[1], il[il[1]], il[1] * il[il[1]])
print(778214, 369089, 287230227046)
#1000 [964823, 792949, 416594] 660104 778214 369089
#778214 369089
#14693.3862114s
