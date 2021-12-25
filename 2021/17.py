from sys import stdin
#from aocd import lines, submit

lines = stdin.read().splitlines()
target = lines[0][15:].split(', ')
tx = tuple(map(int, target[0].split('..')))
ty = tuple(map(int, target[1][2:].split('..')))
print(tx,ty)
s = (1+tx[1]-tx[0])*(1+ty[1]-ty[0])
#s += s//4
for vx0 in range(tx[0]):
    for vy0 in range(-100,200):
        vx = vx0
        vy = vy0
        x,y = 0,0
        my = 0
        for step in range(300):
            x += vx
            y += vy
            if my < y: my = y
            if x > tx[1] or y < ty[0]: break
            if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]:
#                print(vx0, vy0, step, my)
                s += 1
                break
            if vx < 0: vx += 1
            elif vx > 0: vx -= 1
            vy -= 1

print(s)
# submit 2326
