n = 0
ab = "abcdefghijklmnopqrstuvwxyz"
c = [{a:0 for a in ab} for i in range(8)]

while True:
    try: l = input()
    except: break
    for i in range(8):
        c[i][l[i]]+=1

for f in c:
    for k in f:
        if f[k] is min(f.values()):
            print(k, end='')
