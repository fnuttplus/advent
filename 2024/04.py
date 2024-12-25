from sys import stdin
from aocd import get_data, submit
from re import findall

ls = stdin.read().splitlines()

s = 0

for y in range(len(ls)):
    for x in range(len(ls[y])):
        if ls[y][x] == 'X':
            if y+3 < len(ls) and x+3 < len(ls[y]) and ls[y+1][x+1] == 'M':
                if ls[y+2][x+2] == 'A':
                    if ls[y+3][x+3] == 'S':
                        s += 1

            if y+3 < len(ls) and ls[y+1][x] == 'M':
                if ls[y+2][x] == 'A':
                    if ls[y+3][x] == 'S':
                        s += 1

            if y+3 < len(ls) and x-3 >= 0 and ls[y+1][x-1] == 'M':
                if ls[y+2][x-2] == 'A':
                    if ls[y+3][x-3] == 'S':
                        s += 1

            if x-3 >= 0 and ls[y][x-1] == 'M':
                if ls[y][x-2] == 'A':
                    if ls[y][x-3] == 'S':
                        s += 1

            if y-3 >= 0 and x-3 >= 0 and ls[y-1][x-1] == 'M':
                if ls[y-2][x-2] == 'A':
                    if ls[y-3][x-3] == 'S':
                        s += 1

            if y-3 >= 0 and ls[y-1][x] == 'M':
                if ls[y-2][x] == 'A':
                    if ls[y-3][x] == 'S':
                        s += 1

            if y-3 >= 0 and x+3 < len(ls[y]) and ls[y-1][x+1] == 'M':
                if ls[y-2][x+2] == 'A':
                    if ls[y-3][x+3] == 'S':
                        s += 1

            if x+3 < len(ls[y]) and ls[y][x+1] == 'M':
                if ls[y][x+2] == 'A':
                    if ls[y][x+3] == 'S':
                        s += 1

print(s)
