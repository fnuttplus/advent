m = input()
d = []
m0 = [[2]*25 for _ in range(6)]
for x in range(0,len(m),6*25):
    l = m[x:x+6*25]
    for y in range(6):
        for z in range(25):
            i = x + y*25 + z
            if m[i] != "2" and m0[y][z] == 2:
                m0[y][z] = m[i]
    d.append((l.count("0"), l.count("1"), l.count("2")))
d = sorted(d)[0]
print(d[1] * d[2])

for mm in m0:
    print(''.join(["#" if mmm == "1" else " " for mmm in mm]))