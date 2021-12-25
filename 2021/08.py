from sys import stdin
#from aocd import lines, submit
from itertools import permutations

c = 0
lines = stdin.read().splitlines()

p = {
'acedgfb': 8,
'cdfbe': 5,
'gcdfa': 2,
'fbcad': 3,
'dab': 7,
'cefabd': 9,
'cdfgeb': 6,
'eafb': 4,
'cagedb': 0,
'ab': 1,
}
for line in lines:
    a, b = line.split(' | ')
    #b = [len(x) for x in b.split(' ')]
    b = b.split(' ')
    #print(b)
    #c += b.count(2) #1
    #c += b.count(4) #4
    #c += b.count(3) #7
    #c += b.count(7) #8
    a = [''.join(sorted(x)) for x in a.split(' ')]
    #print(a)
    for pp in permutations('abcdefg'):
        for k in p.keys():
            #print(k)
            k =  ''.join(sorted([pp['abcdefg'.index(x)] for x in list(k)]))
            if not k in a:
                break
        else:
            #print(pp)
            n = 0
            for bb in b:
#                print(bb)
                for k in p:
                    k1 =  ''.join(sorted([pp['abcdefg'.index(x)] for x in list(k)]))
                    if k1 == ''.join(sorted(bb)):
                        n = n * 10 + p[k]
#                        print(p[k])
            print(n)
            break
    c += n
"""
in 7, not in 1
in 1, not in sixes
in 4, not in sixes
in sixes
"""
print(c)
