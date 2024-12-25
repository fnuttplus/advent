from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *

s = 0

r = []

t = True
t = False

ls = stdin.read() if t else get_data()

l = [list(x) for x in ls.split('\n')]

g = Grid(l)

x0,y0 = g.find('S')
x1,y1 = g.find('E')
d = (1,0)


"""
The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).
"""

import heapq

# Example grid setup
l = [list(x) for x in ls.strip().split('\n')]
g = Grid(l)

# Starting and ending points
x0, y0 = g.find('S')
x1, y1 = g.find('E')

# Directions: (dx, dy)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North

paths = {}

def backtrack(x,y,direction):
    s = sorted(list(paths[(x,y,direction)].keys()))[0]
    for x,y,direction in paths[(x,y,direction)][s]:
        yield (x,y)
        if (x,y) != (x0,y0):
            for x,y in backtrack(x,y,direction):
                yield (x,y)

def bfs():
    queue = [(0, x0, y0, (1, 0), [])]  # (x, y, direction, score)
    visited = {(x0, y0, (1, 0)): 0}

    while queue:
        score, x, y, direction, path = heapq.heappop(queue)
        if(x,y) == (15,8): print("yesyes", direction, score, )
        if (x, y) == (x1, y1):
            if t:
                for ty in range(len(l)):
                    for tx in range(len(l[0])):
                        if ((tx,ty) in [(p[0], p[1]) for p in path]):
                            print('-',end='')
                        else: print(g[tx,ty], end='')
                    print()
                #print(score)
                #print(visited)
            print(paths)
            path = list(backtrack(x,y,direction))
            for ty in range(len(l)):
                for tx in range(len(l[0])):
                    if ((tx,ty) in path):
                        print('O',end='')
                    else: print(g[tx,ty], end='')
                print()
            return len(set(path))+1
            return score

        # Move forward
        new_x, new_y = x + direction[0], y + direction[1]
        if g[new_x, new_y] != '#':
            if (new_x, new_y, direction) not in visited:
                paths[(new_x, new_y, direction)] = {(score+1): [(x,y,direction)]}
                visited[(new_x, new_y, direction)] = (score+1)
                heapq.heappush(queue, (score + 1, new_x, new_y, direction, path + [(new_x, new_y, direction)]))
            else:
                if visited[(new_x, new_y, direction)] == (score+1):
                    paths[(new_x, new_y, direction)][(score+1)].append([x,y,direction])

        # Rotate clockwise and counterclockwise
        for rotate_dir in [1, -1]:
            new_direction = directions[(directions.index(direction) + rotate_dir) % len(directions)]
            if (x, y, new_direction) not in visited:
                paths[(x, y, new_direction)] = {(score + 1000): [(x,y,direction)]}
                visited[(x, y, new_direction)] = (score + 1000)
                heapq.heappush(queue, (score + 1000, x, y, new_direction, path + [(x, y, new_direction)]))
            else:
                if visited[(x, y, new_direction)] == (score + 1000):
                    paths[(x, y, new_direction)][(score + 1000)].append([x,y,direction])



    return -1  # In case no path is found

# Finding the lowest score
lowest_score = bfs()
print("The lowest score a Reindeer could possibly get is:", lowest_score)


if t:
    print(s)
else:
    submit(lowest_score)
