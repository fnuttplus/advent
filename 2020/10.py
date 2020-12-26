from sys import stdin

l = sorted(list(map(int, stdin.read().splitlines())))
l.append(l[-1] + 3)

d = [2, 4, 7, ]

n, ones, threes = 0, 0, 0
p, streak = 1, 0
for i in l:
    if i - n == 1:
        ones += 1
        streak += 1
    elif i - n == 3:
        threes += 1
#        print(i - n, streak, p)
        if streak > 1:
            p *= d[streak-2]
        streak = 0
    n = i
print(ones, threes, ones * threes)
print(p)
