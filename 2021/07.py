from sys import stdin
#from aocd import lines, submit

lines = stdin.read().splitlines()
numbers = [int(x) for x in lines[0].split(',')]

"""
cc = [0]
for i in range(1, max(numbers)+1):
    cc.append(i+cc[-1])
#print(cc)
"""

def cc(n):
    return (n+1)*n//2

mc = 1000000000000
for i in range(min(numbers), max(numbers)+1):
    c = 0
    for n in numbers:
        c += cc(abs(n-i))
    if c < mc:
        #print(i,mc,c)
        mc = c

print(mc)
