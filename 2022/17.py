from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

ll = stdin.read()
#ll = get_data(day=17)

rocks1 = [
    ['####'],
    ['.#.','###','.#.'],
    ['..#','..#','###'],
    ['#','#','#','#'],
    ['##','##'],
]
walls1 = set()

def rest1(r, x, y):
    if not 0 <= x <= 7-len(r[0]): return True
    if y == -1: return True
    for yy in range(len(r)):
        for xx in range(len(r[0])):
            if r[yy][xx] == '#' and (x+xx,(y+(len(r)-yy))) in walls1:
                return True
    return False

md = 0
def part1(n):
    global walls
    global md
    li = 0
    top = 0
    for ri in range(n):
        r = rocks1[ri%len(rocks1)]
        y = top+3
        x = 2
        while True:
            c = ll[li%len(ll)]
            li += 1
            if c == '<':
                if not rest1(r,x-1,y):
                    x -= 1
            if c == '>':
                if not rest1(r,x+1,y):
                    x += 1
            y -= 1
            if rest1(r, x, y):
                if md < top-y:
                    md = top-y
                    #print(md)
                y += 1
                for yy in range(len(r)):
                    for xx in range(len(r[0])):
                        if r[yy][xx] == '#':
                            walls1.add((x+xx, (y+(len(r)-yy))))
                if y + len(r) > top:
                    top = y + len(r)
                break
    return top

print(part1(2022))
print(md)
"""
for y in range(42,0,-1):
    for x in range(7):
        print('#' if (x,y) in walls1 else '.', end='')
    print()
"""
rocks = [
    ((4,1),((0,0),(1,0),(2,0),(3,0),)),
    ((3,3),((1,-2),(0,-1),(1,-1),(2,-1),(1,0),)),
    ((3,3),((2,-2),(2,-1),(0,0),(1,0),(2,0),)),
    ((1,4),((0,-3),(0,-2),(0,-1),(0,0),)),
    ((2,2),((0,-1),(1,-1),(0,0),(1,0),)),
]
walls = []
top = 0
li = 0
di = 0
def rest(r, x, y):
    if not 0 <= x <= 7-r[0][0]: return True
    if y < 0: return False
    if y >= len(walls): return True
    for dx, dy in r[1]:
        if 0 <= y + dy < len(walls):
            if walls[y+dy][x+dx] == '#':
                return True
    return False

def draw():
    global di
    image = Image.new('L', (9, 17))
    for dy, w in enumerate(walls):
        for dx, ww in enumerate(w):
            if ww == '#':
                image.putpixel((dx+1,dy+7), 200)
    for dx, dy in r[1]:
        image.putpixel((x+dx+1,y+dy+7), 100)
    for dy in range(7+len(walls)):
        image.putpixel((0,dy), 250)
        image.putpixel((8,dy), 250)
    if len(walls) < 10:
        for dx in range(9):
            image.putpixel((dx, 7+len(walls)), 250)
    image = image.resize((8*40,17*40), Image.Resampling.NEAREST)
    image.save("frames/17_"+str(di)+".png")
    di += 1

memo = {}
for ri in range(2022):
    if ri == 459 + 631: print(top, 584795321*(3376-756)+top)
    if (li%len(ll), ri%len(rocks), ''.join([''.join(w) for w in walls])) in memo:
        m = memo[(li%len(ll), ri%len(rocks), ''.join([''.join(w) for w in walls]))]
        print('memo', ri, top, m)
        #2169 3376 (459, 756)
        #54 89 (19, 36)
        print()
        break
    memo[(li%len(ll), ri%len(rocks), ''.join([''.join(w) for w in walls]))] = (ri, top)
    r = rocks[ri%len(rocks)]
    y = -4
    x = 2

    while True:
        c = ll[li%len(ll)]
        li += 1

        if c == '<' and not rest(r,x-1,y): x -= 1
        if c == '>' and not rest(r,x+1,y): x += 1
        draw()
        y += 1
        if rest(r, x, y):
            y -= 1
            if y < r[0][1]:
                for _ in range(r[0][1]-y-1):
                    walls.insert(0, ['.','.','.','.','.','.','.'])
                walls = walls[:md]
                top += r[0][1]-y-1
                y = r[0][1]-1
            for dx, dy in r[1]:
                walls[y+dy][x+dx] = '#'
            walls1 = set()
            draw()
            break

print(top)
