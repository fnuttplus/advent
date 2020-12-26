from sys import stdin

g = [(line[0], int(line[1:])) for line in stdin.read().splitlines()]
#print(g)

d = 'E'
dd = 'NESW'

x, y = 0, 0
dx, dy = 10, -1

for a,b in g:
    #print(a,b)
    if a == "N":
        dy -= b
    elif a == "S":
        dy += b
    elif a == "E":
        dx += b
    elif a == "W":
        dx -= b
    elif a == "L":
        while b > 0:
            b -= 90
            dx, dy = dy, -dx
        #i = (dd.index(d) - b//90) % 4
        #d = dd[i]
    elif a == "R":
        while b > 0:
            b -= 90
            dx, dy = -dy, dx
        #i = (dd.index(d) + b//90) % 4
        #d = dd[i]
    elif a == "F":
        x += b*dx
        y += b*dy
    #print(x, y, dx, dy)
"""        
        if d == 'E':
            x += b
        elif d == 'S':
            y += b
        elif d == 'W':
            x -= b
        elif d == 'N':
            y -= b
"""

print(x + y)