p = list(map(int, list(input())))
b = [0, 1, 0, -1]

for _ in range(100):
    p2 = []
    for i in range(len(p)):
        j = 1
        bb = [v for v in b for _ in range(i+1)]
        #print(i,bb)
        s = 0
        for pp in p:
            #print(pp, bb[j%len(bb)])
            s += pp*bb[j%len(bb)]
            j += 1
        #print(int(str(s)[-1]))
        p2.append(int(str(s)[-1]))
    p = p2[:]
print(p)
