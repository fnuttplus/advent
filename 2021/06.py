from sys import stdin
#from aocd import lines, submit

lines = stdin.read().splitlines()
numbers = [int(x) for x in lines[0].split(',')]

c = [0] * 9
for x in range(1,7):
    c[x] = numbers.count(x)

for d in range(256*256):
    t = c[d%7]
    c[d%7] += c[7]
    c[7] = c[8]
    c[8] = t
    #print(c)

"""
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 6
            numbers.append(8)
        else:
            numbers[i] -= 1
    print(d+1, numbers, n, c)
"""
print(sum(c))
