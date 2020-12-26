from sys import stdin

def match(c):
    global i
    r = rules[c]
    if type(r) is str:
        if i < len(l) and l[i] == r:
            i += 1
            return True
        else: return False
    j = i
    for rr in r[0]:
        if not match(rr):
            if len(r) > 1:
                i = j
                for rr in r[1]:
                    if not match(rr):
                        return False
                return True
            return False
    return True

sections = stdin.read().split("\n\n")

rules = {}
for line in sections[0].split("\n"):
    a,b = line.split(': ')
    if b == "\"a\"": b = 'a'
    elif b == "\"b\"": b = 'b'
    else: b = [list(map(int, bb.split(' '))) for bb in b.split(" | ")]
    rules[int(a)] = b

n = 0
for line in sections[1].split("\n"):
    l = line
    i = 0
    if match(0) and len(l) == i:
        n += 1
print(n)
