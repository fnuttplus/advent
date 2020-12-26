from sys import stdin

l = []
for line in stdin.read().splitlines():
    b = line.replace('F','0').replace('B','1').replace('R','1').replace('L','0')
    l.append(int(b[:7], 2)*8 + int(b[7:], 2))

l = sorted(l, reverse=True)
j = l[0]
print(j)
for i in l[1:]:
    if j - 1 != i:
        print(i + 1)
        break
    j = i
