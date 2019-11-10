from sys import stdin
from os import system

m = [list(l) for l in stdin.read().splitlines()]
c = []
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] in "^<>v":
            c.append([y, x, m[y][x], 0])
            if m[y][x] in "^v": m[y][x] = '|'
            if m[y][x] in "<>": m[y][x] = '-'
    print(''.join(m[y]))

while True:
    for i in range(len(c)):
        if c[i] == []: continue
        y,x,z,w = c[i]
        if z is 'v': y += 1
        elif z is '>': x += 1
        elif z is '^': y -= 1
        elif z is '<': x -= 1
        if m[y][x] is '+':
            z = {'v':">v<", '>':"^>v", '^':"<^>", '<':"v<^"}[z][w]
            w = (w+1)%3
        elif m[y][x] is '/': z = {'v':'<', '>':'^', '^':'>', '<':'v'}[z]
        elif m[y][x] is '\\': z = {'v':'>', '>':'v', '^':'<', '<':'^'}[z]
        c[i] = [y, x, z, w]

        for j in range(len(c)):
            if c[j] == [] or j == i: continue
            if x == c[j][1] and y == c[j][0]:
                c[j] = []
                c[i] = []
                print(str(x)+','+str(y), [cc[:3] for cc in c if cc!=[]])
                break
    c.sort()
    if c.count([]) == 16:
        print(str(c[-1][1]) + ',' + str(c[-1][0]))
        break
