from collections import deque

ins = input().split()
a = int(ins[0])
b = int(ins[6])

c = deque([0])
points = [0] * a
for m in range(1, 100*b+1):
    if m % 23:
        c.rotate(-1)
        c.append(m)
    else:
        c.rotate(7)
        points[(m-2) % a] += m + c.pop()
        c.rotate(-1)

    if m % 1000000 == 0:
        print(m, max(points))

print(max(points))
