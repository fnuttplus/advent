import heapq

class grid():
    def __init__(self, data) -> None:
        self.data = data
    def points(self):
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                yield x, y, self.data[x][y]
    def neighbors(self,x,y):
        for x1,y1 in [(x+1, y),(x-1, y),(x, y+1),(x, y-1),]:
            if 0 <= x1 < len(self.data) and 0 <= y1 < len(self.data[0]):
                yield x1, y1, self.data[x1][y1]
    def neighbors2(self,x,y):
        for x1,y1 in [(x+1, y+1),(x+1, y-1),(x-1, y+1),(x-1, y-1),(x+1, y),(x-1, y),(x, y+1),(x, y-1),]:
            if 0 <= x1 < len(self.data) and 0 <= y1 < len(self.data[0]):
                yield x1, y1, self.data[x1][y1]
    def neighbors3(self,x,y,f):
        for x1,y1 in [(x-1, y-1),(x-1, y),(x-1, y+1),(x, y-1),(x, y),(x, y+1),(x+1, y-1),(x+1, y),(x+1, y+1),]:
            if 0 <= x1 < len(self.data) and 0 <= y1 < len(self.data[0]):
                yield x1, y1, self.data[x1][y1]
            else:
                yield x1,y1, f
    def get2(self,x,y):
        return self.data[x % len(self.data)][y % len(self.data[0])]
    def get(self,x,y):
        return self.data[x][y]
    def set2(self,x,y,n):
        self.data[x % len(self.data)][y % len(self.data[0])] = n
    def set(self,x,y,n):
        self.data[x][y] = n
    def bfs(self, x, y):
        c = [[(10e10,[]) for _ in range(len(self.data[0]))] for _ in range(len(self.data))]
        s = [(0,x,y)]
        c[y][x] = (0,[(x,y)])
        while s:
            n,x,y = s.pop(0)
            for x1,y1,d in self.neighbors(x,y):
                if c[y1][x1][0] > n + d:
                    c[y1][x1] = (n + d, c[y][x][1] + [(x1,y1)])
                    heapq.heappush(s,(n + d, x1, y1))
        return c
    def imageData(self):
        return [(100,100,100) if self.data[y][x] == "#" else (10,10,10) for y in range(len(self.data)) for x in range(len(self.data[0]))]
    def imageData2(self):
        return [(self.data[y][x]*20, self.data[y][x]*20, self.data[y][x]*20) for y in range(len(self.data)) for x in range(len(self.data[0]))]
    def __repr__(self):
        return '\n'.join([''.join(map(str,x)) for x in self.data])

class matrix():
    def __init__(self):
        self.data = []
    
    def fromLines(self, lines, sep = ''):
        if sep != '':
            self.data = [[int(x) for x in line.split(sep) if x] for line in lines]
        else:
            self.data = [list(line) for line in lines]
    def rotation(self):
        return list(zip(*self.data[::-1]))
    def bingo(self, n):
        self.data = [[None if x == n else x for x in r] for r in self.data]
    def sum(self):
        s = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                if self.data[x][y] != None:
                    s += self.data[x][y]
        return s
    def __repr__(self):
        return str(self.data)