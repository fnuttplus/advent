from sys import stdin

def gen(c):
    r = rules[c]
    if type(r) is str: yield r
    else:
        for g0 in gen(r[0][0]):
            if len(r[0]) > 1:
                for g1 in gen(r[0][1]):
                    yield g0+g1
            else: yield g0
        if len(r) > 1:
            for g0 in gen(r[1][0]):
                if len(r[0]) > 1:
                    for g1 in gen(r[1][1]):
                        yield g0+g1
                else: yield g0

sections = stdin.read().split("\n\n")

rules = {}
for line in sections[0].split("\n"):
    a,b = line.split(': ')
    if b == "\"a\"": b = 'a'
    elif b == "\"b\"": b = 'b'
    else: b = [list(map(int, bb.split(' '))) for bb in b.split(" | ")]
    rules[int(a)] = b

#rules[8] = [[42], [42, 8]]
#rules[11] = [[42, 31], [42, 11, 31]]
l42 = list(gen(42))
l31 = list(gen(31))

n = 0
for l in sections[1].split("\n"):
    starts = 0
    while True:
        for a in l42:
            if l.startswith(a):
                starts += 1
                l = l[len(a):]
                break
        else:
            break
    if l == "": continue
    ends = 0
    while True:
        for a in l31:
            if l.endswith(a):
                ends += 1
                l = l[:-len(a)]
                break
        else:
            break
    if l == "" and starts > ends:
        n += 1
print(n)
