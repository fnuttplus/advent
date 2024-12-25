from PIL import Image
from sys import stdin
from random import random
from collections import Counter
from oklab import viridis, turbo

class Grid():
    def __init__(self, data = []) -> None:
        self.data = data
    def __getitem__(self, t):
        return self.data[t[1]][t[0]]
    def __setitem__(self, t, v):
        self.data[t[1]][t[0]] = v
    def from_stdin(self):
        self.data = [list(x) for x in stdin.read().splitlines()]
        return self
    def xy(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                yield x, y
    def fit(self, x, y):
        return 0 <= y < len(self.data) and 0 <= x < len(self.data[0])
    def x(self):
        return len(self.data[0])
    def y(self):
        return len(self.data)
    def find(self, i):
        for x, y in self.xy():
            if self[x,y] == i:
                return x, y
    def find_all(self, i):
        for x, y in self.xy():
            if self[x,y] == i:
                yield x, y
    def flood_fill(self, x0, y0, i, o):
        q = [(x0, y0)]
        while q:
            (x,y) = q.pop()
            self.data[y][x] = o
            for x1,y1 in [(x+1, y),(x-1, y),(x, y+1),(x, y-1),]:
                if self.fit(x1, y1) and self.data[y1][x1] == i:
                    q.append((x1,y1))
    def image_data(self, d):
        return [d[self[x,y]] for y in range(self.y()) for x in range(self.x())]
    def __repr__(self):
        return '\n'.join([''.join(map(str,x)) for x in self.data])

    def rows(self):
        for i, row in enumerate(self.data):
            yield i, row
    def cols(self):
        for i in range(len(self.data[0])):
            col = [self.data[y][i] for y in range(len(self.data))]
            yield i, col

    def xy_rd(self):
        for y in range(self.y()):
            for x in range(self.x()):
                yield x, y
    def xy_dr(self):
        for x in range(self.x()):
            for y in range(self.y()):
                yield x, y
    def xy_ru(self):
        for y in range(self.y()-1,-1,-1):
            for x in range(self.x()):
                yield x, y
    def xy_dl(self):
        for x in range(self.x()-1,-1,-1):
            for y in range(self.y()):
                yield x, y

    def count(self, c):
        return sum([1 for x,y in self.xy() if self.data[y][x] == c])
    def save_image(self, xx):
        d = Counter([self.data[y][x] for x,y in self.xy()])
        d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
        l = len(d)
        v = viridis(l)
        i = 0
        for dd in d:
            d[dd] = v[i]
            i += 1
        self.save_image_file(d, f"frames/advent{xx}.png")
    def save_image_file(self, d, filename):
        image = Image.new('RGB', (self.x(), self.y()))
        image.putdata(self.image_data(d))
        image2 = image.resize((8*self.x(), 8*self.y()), Image.Resampling.NEAREST)
        image2.save(filename)
    def copy(self):
        return Grid([list(x) for x in str(self).splitlines()])
    def swap(self, x0,y0, x1,y1):
        self[x0,y0], self[x1,y1] = self[x1,y1], self[x0,y0]
    def bfs(self, x0,y0, x1,y1):
        visited = set([(x0,y0)])
        s = [(x0, y0, [(x0, y0)])]
        while s:
            ns = []
            for x,y,path in s:
                if (x, y) == (x1, y1):
                    return path
                for dx,dy in directions:
                    if self.fit(x+dx, y+dy) and self[x+dx, y+dy] == '.' and not (x+dx, y+dy) in visited:
                        visited.add((x+dx, y+dy))
                        ns.append((x+dx, y+dy, path+[(x+dx, y+dy)]))
            s = ns
        return []
    def bfs2(self, pos, target):
        s = [(pos[0], pos[1], [], [pos])]
        while s:
            ns = []
            for x,y,path,visited in s:
                if (x, y) == target:
                    yield path
                for dx,dy in directions:
                    if self.fit(x+dx, y+dy) and self[x+dx, y+dy] != '' and not (x+dx, y+dy) in visited:
                        ns.append((x+dx, y+dy, path+[(dx, dy)], visited+[(x+dx, y+dy)]))
            s = ns
        return []
def adj(x, y):
    return [(x+1, y),(x-1, y),(x, y+1),(x, y-1),]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North
