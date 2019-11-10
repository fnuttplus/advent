from sys import stdin

g = [[0] * 300 for _ in range(300)]
s = 6392
for y in range(1,301):
    for x in range(1,301):
        r =x+10 
        g[y-1][x-1] = (r*(y*r+s)//100)%10-5

m = 0
for z in range(1, 301):
    print(z)
    for y in range(301-z):
        for x in range(301-z):
            n = sum([g[y+i][x+j] for i in range(z) for j in range(z)])
            if n > m:
                m = n
                print(m, x+1, y+1, z)

for y in range(my-1,my+4):
    print(g[y][mx-1:mx+4])