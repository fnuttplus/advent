from sys import stdin
from aocd import get_data, submit
from re import findall

ls = stdin.read().splitlines()

s = 0

for y in range(1, len(ls) -1):
    for x in range(1, len(ls[y]) -1):
        if ls[y][x] == 'A':
            if ls[y+1][x+1] == 'M' and ls[y-1][x-1] == 'S':
                if ls[y-1][x+1] == 'M' and ls[y+1][x-1] == 'S':
                    s += 1

                if ls[y-1][x+1] == 'S' and ls[y+1][x-1] == 'M':
                    s += 1

            if ls[y+1][x+1] == 'S' and ls[y-1][x-1] == 'M':
                if ls[y-1][x+1] == 'M' and ls[y+1][x-1] == 'S':
                    s += 1

                if ls[y-1][x+1] == 'S' and ls[y+1][x-1] == 'M':
                    s += 1

print(s)
