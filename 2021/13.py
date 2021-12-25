from sys import stdin
#from aocd import lines, submit

lines = stdin.read().split("\n\n")
ins = lines[1].splitlines()
lines = lines[0].splitlines()

n = 1500
mx,my = 0,0
g = [["." for _ in range(n)] for _ in range(n)]
for line in lines:
    a,b = map(int, line.split(","))
    g[b][a] = "#"
    if a > mx: mx = a
    if b > my: my = b
#print(mx,my)

for i in ins:
    a,b = i.split("=")
    a = a[-1]
    b = int(b)
    for y in range(b if a == 'y' else 0,my + 1):
        for x in range(b if a == 'x' else 0,mx + 1):
            if g[y][x] == "#":
                if a == 'y': g[2*b-y][x] = "#"
                if a == 'x': g[y][2*b-x] = "#"
    if a == 'y': my = b
    if a == 'x': mx = b

    #print(sum([gg[:mx+1].count('#') for gg in g[:my+1]]))
    #break

print('\n'.join([''.join(map(str,x[:mx])) for x in g[:my]]))
print("RHALRCRA")
