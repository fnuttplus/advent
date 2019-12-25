from sys import stdin
import json

d = {}
for line in stdin.read().splitlines():
    r = line.split(" ")
    d[r[-1]] = (int(r[-2]), [(r[i+1].replace(',',''), int(r[i])) for i in range(0,len(r) - 3,2)])

bank = {}
mem = []
def rec(m, n):
    #print(m,n,bank)
    if n < 1: return 0
    if m == "ORE": return n
    nn = 0
    f = -(-n//d[m][0])
    for mm in d[m][1]:
        try:
            i = min(mm[1] * f, bank[mm[0]])
            bank[mm[0]] -= i
        except: i = 0
        nn += rec(mm[0], mm[1] * f - i)
    try: bank[m] += n % d[m][0]
    except: bank[m] = n % d[m][0]
    return nn

n,i = 0,1896688
while n < 1000000000000:
    n = rec("FUEL", i)
    print(i,n)
    i += 1
