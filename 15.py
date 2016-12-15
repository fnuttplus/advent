#l = [l.split() for l in open('15.in').readlines()]
#discs = [(int(l[i][3]),int(l[i][-1][:-1]) + i+1) for i in range(len(l))]
discs = [(101,3),(163,9),(263,13),(293,6),(373,14),(499,6),(577,7)]
i,t = 1,0
for p,s in discs:
    while (s+t)%p: t += i
    i *= p
print(t) #60564135607891726
