from sys import stdin

n = 0
for l in stdin.read().splitlines():
    x,y,z = l.split(' ')
    i,j = map(int, x.split('-'))
    c = y[0]
    #if i <= z.count(c) <= j: n+=1
    if z[i-1] == c or z[j-1] == c:
        if z[i-1] != z[j-1]:
            n += 1
print(n)
