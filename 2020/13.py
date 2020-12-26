from sys import stdin

g = stdin.read().splitlines()
a = int(g[0])
a0 = a
b = g[1].split(',')
for i,v in enumerate(b):
    if v == 'x': continue
    v = int(v)
    print(i, v, v - a % v)
    if i == 0:
        m = v
        x = m
        continue
    while x % v != (v-i) % v:
        x += m
    m *= v
print(x)

# part 2
x = 45792826502776
while True:
    if x % 23 == (23-73) % 23:
        print(x)
        break
    x += 19 * 41 * 523 * 17 * 13 * 29 * 853 * 37

# part 1
while True:
    for c in b:
        if c != 'x':
            #print(c)
            c = int(c)
            if a % c == 0:
                print(a - a0, c)
                print((a - a0) * c)
                break
    else:
        a += 1
        continue
    break
