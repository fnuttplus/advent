from sys import stdin

lines = stdin.read().splitlines()

class region:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.x1 = x[0]
        self.x2 = x[1]
        self.y1 = y[0]
        self.y2 = y[1]
        self.z1 = z[0]
        self.z2 = z[1]
    def setX(self,a,b):
        self.x = (a,b)
        self.x1 = a
        self.x2 = b
    def setY(self,a,b):
        self.y = (a,b)
        self.y1 = a
        self.y2 = b
    def setZ(self,a,b):
        self.z = (a,b)
        self.z1 = a
        self.z2 = b

def parse_region(line):
    a,b = line.split(' ')
    x,y,z = b.split(',')
    x = tuple(map(int, x[2:].split('..')))
    y = tuple(map(int, y[2:].split('..')))
    z = tuple(map(int, z[2:].split('..')))
    return region(x,y,z)

def split(a, b):
    if a.x2 < b.x1 or b.x2 < a.x1 or a.y2 < b.y1 or b.y2 < a.y1 or a.z2 < b.z1 or b.z2 < a.z1:
        yield a

    elif a.x1 < b.x1 <= a.x2:
        yield region((a.x1, b.x1-1), a.y, a.z)
        a.setX(b.x1, a.x2)
        for nr in split(a, b): yield nr
    elif a.x1 <= b.x2 < a.x2:
        yield region((b.x2+1, a.x2), a.y, a.z)
        a.setX(a.x1, b.x2)
        for nr in split(a, b): yield nr

    elif a.y1 < b.y1 <= a.y2:
        yield region(a.x, (a.y1, b.y1-1), a.z)
        a.setY(b.y1, a.y2)
        for nr in split(a, b): yield nr
    elif a.y1 <= b.y2 < a.y2:
        yield region(a.x, (b.y2+1, a.y2), a.z)
        a.setY(a.y1, b.y2)
        for nr in split(a, b): yield nr

    elif a.z1 < b.z1 <= a.z2:
        yield region(a.x, a.y, (a.z1, b.z1-1))
        a.setZ(b.z1, a.z2)
        for nr in split(a, b): yield nr
    elif a.z1 <= b.z2 < a.z2:
        yield region(a.x, a.y, (b.z2+1, a.z2))
        a.setZ(a.z1, b.z2)
        for nr in split(a, b): yield nr

    elif not (b.x1 <= a.x1 and b.x2 >= a.x2 and b.y1 <= a.y1 and b.y2 >= a.y2 and b.z1 <= a.z1 and b.z2 >= a.z2):
        yield a

onregions = [parse_region(lines[0])]

for line in lines[1:20]: # :20
    r = parse_region(line)
    newregions = []
    for rr in onregions:
        for nr in split(rr, r):
            newregions.append(nr)
    if line[1] == 'n':
        newregions.append(r)
    onregions = newregions

def volume(r): return (r.x2+1 - r.x1) * (r.y2+1 - r.y1) * (r.z2+1 - r.z1)
print(sum([volume(r) for r in onregions]))

for r in onregions:
    print(f'create_mesh({r.x[0]}.0, {r.x[1]+1}.0, {r.y[0]}.0, {r.y[1]+1}.0, {r.z[0]}.0, {r.z[1]+1}.0),')
