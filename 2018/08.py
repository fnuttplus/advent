from sys import stdin

ins = list(map(int, input().split()))

n = [[{} for _ in range(ins[0])], ins[1]]
i = 2
p = [n]
s = 0
while i < len(ins):
    for dd in range(len(n[0])):
        if n[0][dd] == {}:
            n[0][dd] = [[{} for _ in range(ins[i])], ins[i+1]]
            p.append(n)
            n = n[0][dd]
            i += 2
            break
    else:
        i += n[1]
        l = ins[i-n[1]:i]
        s += sum(l)
        if n[0] == []:
            n[1] = sum(l)
        else:
            n[1] = sum([n[0][ii-1][1] for ii in l if ii > 0 and ii <= len(n[0])])
        n = p.pop()

print(s)
print(n[1])
