from sys import stdin
#from aocd import lines, submit

lines = stdin.read().splitlines()

d = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
p = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}
p1 = 0
p2 = []
for line in lines:
    stack = []
    for c in line:
        if c in d:
            stack.append(c)
        else:
            cc = stack.pop()
            if c != d[cc]:
                p1 += p[c]
                print("Expected", cc, "found", c)
                break
    else:
        pc = 0
        for c in stack[::-1]:
            pc = pc * 5 + p[c]
        print(''.join(d[x] for x in stack[::-1]), pc, "points")
        p2.append(pc)

print()
print(p1)
print(sorted(p2)[len(p2)//2])

# submit