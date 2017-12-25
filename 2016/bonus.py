#day25
from sys import stdin
ins = [l.split() for l in stdin.read().splitlines()]

def val(v): return reg[v] if v in reg else int(v)

nextinput = ""

ip = 0
reg = {a:0 for a in "abcde"}
while ip < len(ins):
    i,a,b = ins[ip][0],ins[ip][1],ins[ip][-1]
    ip += 1
    if   i == "cpy": reg[b] = val(a)
    elif i == "inc": reg[a] += 1
    elif i == "dec": reg[a] -= 1
    elif i == "jnz" and val(a): ip += val(b)-1
    elif i == "out": nextinput += chr(val(a))

print(nextinput)
ins = [l.split() for l in nextinput.splitlines()]

#day08
screen = [[' ' for y in range(50)] for y in range(6)]
n = 0
ip = 0
while ip < len(ins):
    ex = ins[ip]
    ip += 1
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

print('\n'.join(''.join(row) for row in screen))
