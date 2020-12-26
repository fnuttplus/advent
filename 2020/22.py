from sys import stdin

p1, p2 = [list(map(int, ss.split("\n")[1:])) for ss in stdin.read().split("\n\n")]

print(32856, 33805)

d = 0
def rec(p1, p2):
    mem = set()
    while True:
        k = (str(p1), str(p2))
        if k in mem: return True, 0
        mem.add(k)

        a = p1.pop(0)
        b = p2.pop(0)

        if a <= len(p1) and b <= len(p2):
            p1w, _ = rec(p1[:a], p2[:b])
        else: p1w = a > b

        if p1w: p1 += [a,b]
        else: p2 += [b,a]

        if len(p2) == 0: return True, p1
        if len(p1) == 0: return False, p2

_, p = rec(p1, p2)

n = sum([(len(p) - i) * v for i,v in enumerate(p)])
print(n)
