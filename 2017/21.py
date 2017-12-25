from sys import stdin

data = stdin.read().splitlines()
rules = []
for row in data:
    row = row.split(' => ')
    rules.append((row[0].split('/'), row[1].split('/')))

def rot(rule):
    return [''.join(row) for row in zip(*rule[::-1])]

def flip(rule):
    return rule[::-1]

image = ['.#.','..#','###']

def match(image, rule):
    for y in range(len(image)):
        for x in range(len(image[y])):
            if rule[y][x] != image[y][x]:
                return False
    return True

def transformation(image):
    yield image
    for _ in range(3):
        image = rot(image)
        yield image
    image = flip(image)  
    yield image
    for _ in range(3):
        image = rot(image)
        yield image

def enhance(image):
    for image in transformation(image):
        for rule in rules:
            pattern = rule[0]
            if len(pattern) != len(image): continue
            if match(image, pattern): return rule[1]

image = enhance(image)

for _ in range(17):
    #print('\n'.join(image))
    if len(image) % 2 == 0:
        x = len(image)//2
        newimages = []
        for i in range(0, len(image), 2):
            for j in range(0, len(image), 2):
                newimages.append([image[i][j:j+2],image[i+1][j:j+2]])
    elif len(image) % 3 == 0:
        x = len(image)//3
        newimages = []
        for i in range(0, len(image), 3):
            for j in range(0, len(image), 3):
                newimages.append([image[i][j:j+3],image[i+1][j:j+3],image[i+2][j:j+3]])
    for i in range(len(newimages)):
        newimages[i] = enhance(newimages[i])
    image = []
    for yy in range(x):
        image += [''.join(newimages[y+yy*x][z] for y in range(x)) for z in range(len(newimages[0]))]

print('\n'.join(image).count('#'))
