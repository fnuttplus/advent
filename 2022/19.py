from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

#ll = stdin.read().splitlines()
ll = get_data(day=19).splitlines()

c = 0
bp = []
for l in ll:
    s = l.split('costs ')
    bp.append((
        int(s[1].split(' ')[0]),
        int(s[2].split(' ')[0]),
        (int(s[3].split(' ')[0]), int(s[3].split(' ')[3])),
        (int(s[4].split(' ')[0]), int(s[4].split(' ')[3])),
    ))
print(bp)

"""
def sim(i, m0, m1, m2, m3, m4, m5):
    ore = 0
    r0, r1, r2, r3 = 1, 0,0,0
    n1, n2, n3 = 0,0,0
    for m in range(24):
#        print(m)
        d0 = r0
        d1 = r1
        d2 = r2
        d3 = r3
        if ore >= bp[i][3][0] and n2 >= bp[i][3][1]:
#            print('buy3')
            r3 += 1
            ore -= bp[i][3][0]
            n2 -= bp[i][3][1]
        elif (m5 < m < m1) and ore >= bp[i][2][0] and n1 >= bp[i][2][1]:
#            print('buy2')
            r2 += 1
            ore -= bp[i][2][0]
            n1 -= bp[i][2][1]
        elif (m2 < m < m3 or m == m0) and ore >= bp[i][1]:
#            print('buy1')
            r1 += 1
            ore -= bp[i][1]
        elif (m < m4) and ore >= bp[i][0]:
#            print('buy0')
            r0 += 1
            ore -= bp[i][0]
        ore += d0
        n1 += d1
        n2 += d2
        n3 += d3
#        print(ore,n1,n2,n3)
#        print(r0,r1,r2,r3)
    return n3

#sim(1,0,21,0,15,7)
#sim(0,15,11,7,0)
#exit()
s = 0
for i in range(len(bp)):
    ma = 0
    for m5 in range(24):
        for m2 in range(24):
            for m4 in range(m2,24):
                for m3 in range(m4,24):
                    for m1 in range(m3,24):
                        for m0 in range(m1,24):
                            d = sim(i,m0,m1,m2,m3,m4,m5)
                            if d > ma:
                                #print(m0,m1,m2,m3,m4,m5, d)
                                ma = d
    print(i+1, ma)
    s += ma * (i+1)
print(s)
"""

ma = 0
memo = set()
def rec(i, m, ore, clay, obs, geo, oreBots, clayBots, obsBots, geoBots, path):
    global ma
    if (i, m, ore, clay, obs, geo, oreBots, clayBots, obsBots, geoBots) in memo: return
    memo.add((i, m, ore, clay, obs, geo, oreBots, clayBots, obsBots, geoBots))
    oreCost, clayCost, obsCost, geoCost = bp[i]
    if m == 32:
        if geo > ma:
            ma = geo
            print(i, ma, path)
        return
    if ore >= geoCost[0] and obs >= geoCost[1]:
        rec(i, m+1, ore-geoCost[0]+oreBots, clay+clayBots, obs-geoCost[1]+obsBots, geo+geoBots, oreBots, clayBots, obsBots, geoBots+1, path+['geo'])
    else:
        rec(i, m+1, ore+oreBots, clay+clayBots, obs+obsBots, geo+geoBots, oreBots, clayBots, obsBots, geoBots, path+['0'])
        if ore >= obsCost[0] and clay >= obsCost[1]:
            rec(i, m+1, ore-obsCost[0]+oreBots, clay-obsCost[1]+clayBots, obs+obsBots, geo+geoBots, oreBots, clayBots, obsBots+1, geoBots, path+['obs'])
        if ore >= clayCost:
            rec(i, m+1, ore-clayCost+oreBots, clay+clayBots, obs+obsBots, geo+geoBots, oreBots, clayBots+1, obsBots, geoBots, path+['clay'])
        if m < 15 and ore >= oreCost:
            rec(i, m+1, ore-oreCost+oreBots, clay+clayBots, obs+obsBots, geo+geoBots, oreBots+1, clayBots, obsBots, geoBots, path+['ore'])

s = 0
for i in range(len(bp)):
    memo=set()
    ma = 0
    rec(i,0,0,0,0,0,1,0,0,0,[])
    print(i+1, ma)
    s += (i+1)*ma
print(s)

#rec(2,0,0,0,0,0,1,0,0,0,[])
