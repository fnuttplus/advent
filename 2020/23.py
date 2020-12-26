l = list(map(int, list(input())))
#print(l)
m = max(l)

for _ in range(100):
    #if l[0] == 10: print(l)
    t = l[1:4]
    i = l[0]-1
    l = [l[0]] + l[4:]
    if i == 0: i = m
    while i in t:
        i -= 1
        if i == 0: i = m
    d = l.index(i)+1
    l = l[1:d] + t + l[d:] + [l[0]]

i = l.index(1)
l = l[i+1:]+l[:i]
print(''.join(map(str, l)))
