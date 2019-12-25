i = input()
p = (list(map(int,list(i)))*10000)[int(i[:7]):]

for n in range(100):
    s = sum(p)
    for i in range(len(p)):
        p[i], s = s%10, s-p[i]
    if n % 10 == 9:
        print(n+1, ''.join(map(str, p[:8])))
