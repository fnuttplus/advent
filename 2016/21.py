def rotate(l,x):
    x = x%len(l)
    return l[-x:] + l[:-x]

def scramble(s):
    l = list(s)
    for i in ins:
        if i[0] == "rotate":
            if i[1] == "based":
                a = l.index(i[-1])
                if a >= 4: a += 2
                else: a += 1
                l= rotate(l,a)

            else:
                a = int(i[2])
                if i[1] == "left": l = rotate(l,-a)
                else: l = rotate(l,a)

        elif i[0] == "swap":
            if i[1] == "position":
                a = int(i[2])
                b = int(i[5])
                l[a],l[b] = l[b],l[a] 
            
            else:
                a = l.index(i[2])
                b = l.index(i[5])
                l[a],l[b] = l[b],l[a]
        
        elif i[0] == "move":
            a = int(i[2])
            b = int(i[5])
            l.insert(b,l.pop(a))

        elif i[0] == "reverse":
            a = int(i[2])
            b = int(i[4])
            l = l[:a] + list(reversed(l[a:b+1])) + l[b+1:]

    return ''.join(l)

from sys import stdin
from itertools import permutations

ins = [l.split() for l in stdin.read().splitlines()]

print(scramble("abcdefgh"))
for p in permutations("abcdefgh"):
    if scramble(p) == "fbgdceah":
        print(''.join(p))
