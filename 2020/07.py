from sys import stdin

d = {}
for line in stdin.read().splitlines():
    ls = line.split()
    if ls[4] == 'no': continue
    d[(ls[0], ls[1])] = []
    for i in range(4, len(ls), 4):
        #print(ls[i])
        d[(ls[0], ls[1])].append((ls[i], ls[i+1], ls[i+2]))

i = 0
def find(a, b, s):
    global i
    i += 1
    #print(a, b)
    for dd in d:
        #print(dd, d[dd])
        for ddd in d[dd]:
            if ddd[1] == a and ddd[2] == b:
                if not dd in s:
                    s.add(dd)
                    find(dd[0], dd[1], s)

def c(a, b):
    s = 1
    for dd in d:
        if dd[0] == a and dd[1] == b:
            for ddd in d[dd]:
                #print(ddd)
                s += int(ddd[0]) * c(ddd[1], ddd[2])
    return s

find('shiny', 'gold', set())
print(i-1)
print(c('shiny', 'gold')-1)
