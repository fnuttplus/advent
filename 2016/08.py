screen = [[' ' for y in range(50)] for y in range(6)]
n = 0
while True:
    try: ex = input().split()
    except: break
    if ex[0] == 'rect':
        x,y = map(int,ex[1].split('x'))
        n += x*y
        for yy in range(y):
            for xx in range(x):
                screen[yy][xx] = '@'
    elif ex[0] == 'rotate':
        if ex[1] == 'column':
            x = int(ex[2].split('=')[1])
            y = int(ex[4])
            c = [row[x] for row in screen]
            c = c[-y:]+c[:-y]
            for yy in range(6):
                screen[yy][x] = c[yy]
        elif ex[1] == 'row':
            y = int(ex[2].split('=')[1])
            x = int(ex[4])
            screen[y] = screen[y][-x:] + screen[y][:-x] 
print(n)
print('\n'.join(''.join(row) for row in screen))
