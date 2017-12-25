from sys import stdin

bl = sorted([tuple(map(int,l.split('-'))) for l in stdin.read().splitlines()])
ranges = []
x = 0
for r in bl:
    a,b = r
    if a <= x:
        if x <= b:
            x = b+1
    else:
        if b == 4294967295:
            ranges.append([x,a-1])
            break
        else:
            ranges.append([a-1,x])
            x = b+1

print(ranges[0][0])
print(sum([b+1-a for a,b in ranges]))
