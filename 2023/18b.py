from sys import stdin
from re import findall
from aoc import Grid
import heapq

lines = stdin.read().splitlines()
from PIL import Image
image = Image.new('RGB', (354 + 40 + 1, 137 + 171 + 1), (9, 38, 53))

s = 0
x,y = 0,0
for line in lines:
    a,b,c = line.split(' ')
    b = int(b)
    c = c[2:-1]
    print(a,b,c, tuple(int(c[i:i+2], 16) for i in (0, 2, 4)))
    d = {
        'R': (1,0),
        'L': (-1,0),
        'D': (0,1),
        'U': (0,-1)
    }[a]
    for i in range(b):
        x += d[0]
        y += d[1]
        image.putpixel((40 + x, 171 + y), tuple(int(c[i:i+2], 16) for i in (0, 2, 4)))

image2 = image.resize((2*image.width, 2*image.height), Image.Resampling.NEAREST)
image2.save("2023.18.png")
