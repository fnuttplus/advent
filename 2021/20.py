from sys import stdin, setrecursionlimit
from aocd import lines, submit
from aoc import grid
#from aocd import numbers
from itertools import permutations, combinations, product
from math import prod
from collections import Counter
from re import finditer, search
from PIL import Image

#setrecursionlimit(10000)

#ab = "abcdefghijklmnopqrstuvwxyz".upper()

lines = stdin.read().splitlines()
#numbers = [int(x) for x in lines[0].split(',')]
ss = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
ss = "##..##...#...##.##...##.##..####....##...##.#.######....###.##...##.##....#..#..###..##.##.###.#..##.###.#......##.#####..#...#...#.#.....#.###.#..#######....##.##.#.#.....##.#.##...#...###.####.#.#####...#..#..#######....#..##.....##.##.#####.####.....#...##..#..#.###....#..##.#....##.##..###...##.##.##.####....##.#...#.#.#.###########...###.###.#.#.###..##.######...#..#.##.......##.#.###....#..##....#.#..##..##..###.#...#.##.#..##..##..####.#.##.#.....###.#..####....#..##...##.##..###...#...#..##..#.#..#."
n = 25
gg = [['.' for _ in range(2*n)] + list(line) + ['.' for _ in range(2*n)] for line in lines]
for _ in range(n):
    gg.insert(0,['.' for _ in range(len(lines[0])+4*n)])
    gg.insert(0,['.' for _ in range(len(lines[0])+4*n)])
    gg.append(['.' for _ in range(len(lines[0])+4*n)])
    gg.append(['.' for _ in range(len(lines[0])+4*n)])

print(gg)
g = grid([ggg.copy() for ggg in gg])
g1 = grid([ggg.copy() for ggg in gg])
print(g)
image = Image.new('RGB', (len(gg[0]), len(gg)))
image.putdata(g.imageData())
image = image.resize((len(gg[0])*10,10*len(gg)),Image.NEAREST)
image.save("frames/20_0.png")
for step in range(n):
    for x,y,n in g.points():
        #print(x,y,n,''.join([n for _,_,n in g.neighbors3(x,y)]))
        n1 = int(''.join(['1' if n is '#' else '0' for _,_,n in g.neighbors3(x,y,".")]), 2)
        #print(n1,ss[n1])
        g1.set(x,y,ss[n1])
    print(g1)
    image = Image.new('RGB', (len(gg[0]), len(gg)))
    image.putdata(g1.imageData())
    image = image.resize((len(gg[0])*10,10*len(gg)),Image.NEAREST)
    image.save("frames/20_"+str(2*step+1)+".png")

    g1,g = g,g1
    for x,y,n in g.points():
        #print(x,y,n,''.join([n for _,_,n in g.neighbors3(x,y)]))
        n1 = int(''.join(['1' if n is '#' else '0' for _,_,n in g.neighbors3(x,y,"#")]), 2)
        #print(n1,ss[n1])
        g1.set(x,y,ss[n1])
    print(g1)

    image = Image.new('RGB', (len(gg[0]), len(gg)))
    image.putdata(g1.imageData())
    image = image.resize((len(gg[0])*10,10*len(gg)),Image.NEAREST)
    image.save("frames/20_"+str(2*step+2)+".png")
    g1,g = g,g1

c = 0
for _,_,n in g.points():
    if n is '#': c += 1
print(c)
# submit