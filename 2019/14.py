from sys import stdin
import json

d = {}
for line in stdin.read().splitlines():
    r = line.split(" ")
    d[r[-1]] = (int(r[-2]), [(r[i+1].replace(',',''), int(r[i])) for i in range(0,len(r) - 3,2)])

bank = {}
def rec(m, n):
    if m == "ORE": return n
    try: i = bank[m]
    except: i = 0
    bank[m] = 0
    nn = 0
    while i < n:
        i += d[m][0]
        for mm in d[m][1]:
            nn += rec(mm[0], mm[1])
    if i > n:
        bank[m] += i-n
    return nn

print(d)
print(1896688)
n,i = 0,0
while n < 1000000000000:
    i += 100
    n += rec("FUEL", 100)
    print(i,n,bank)
