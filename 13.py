def oo(x,y): return bin(x*x+3*x+2*x*y+y+y*y+1358).count('1')&1

room = [['#' if oo(x,y) else ' ' for x in range(37)] for y in range(44)]
room[39][31] = '$'
room[1][1] = '@'
n = [(1,1)]
d = 0
i = 1
while n:
    d += 1
    nn = []
    for y,x in n:
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= y+dy < len(room) and 0 <= x+dx < len(room[0]):
                if room[y+dy][x+dx] is ' ':
                    if d <= 50: i += 1
                    room[y+dy][x+dx] = '+' if d<=50 else '-'
                    nn.append((y+dy,x+dx))
                elif room[y+dy][x+dx] is '$':
                    print(d)
    n = nn

print(i)
for r in room: print(''.join(map(str,r)))
