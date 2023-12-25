from sys import stdin
from re import findall
from aoc import Grid
import heapq
import time

#g = Grid().from_stdin()

lines = stdin.read().split('\n\n')
wfs = {wf.split('{')[0]: wf.split('{')[1][:-1].split(',') for wf in lines[0].splitlines()}
parts = lines[1].splitlines()

for wf in wfs:
    for i in range(len(wfs[wf])):
        rule = wfs[wf][i]
        #print(rule)
        a = rule[0]
        isCompare = True
        next = ''
        if not ':' in rule:
            isCompare = False
            next = rule
        elif a in 'xmas':
            c = rule[1]
            n = int(rule.split(':')[0][2:])
            next = rule.split(':')[1]
        wfs[wf][i] = {
            'isCompare': isCompare,
            'next': next,
            'a': a,
            'c': c,
            'n': n,
        }
print(wfs)

def accept(wf, part):
#    print(part)
    for rule in wfs[wf]:
#        print(rule)
        if not rule['isCompare']:
            if rule['next'] == 'A':
                return True
            if rule['next'] == 'R':
                return False
            return accept(rule['next'], part)
        a = False
        if rule['c'] == '>':
            if part[rule['a']] > rule['n']:
                a = True
        elif rule['c'] == '<':
            if part[rule['a']] < rule['n']:
                a = True
        if a:
            if rule['next'] == 'R':
                return False
            if rule['next'] == 'A':
                return True
            return accept(rule['next'], part)

def accept1(wf, part):
    #print(wf, part)
    for rule in wfs[wf]:
        c = rule[0]
        if not ':' in rule:
    #        print(c, rule)
            if c == 'A':
                return True
            if c == 'R':
                return False
            return accept(rule, part)
        if c in 'xmas':
            n = int(rule.split(':')[0][2:])
            l = rule.split(':')[1]
            a = False
            if rule[1] == '>':
                if part[c] > n:
                    a = True
            elif rule[1] == '<':
                if part[c] < n:
                    a = True
            if a:
                if l == 'R':
                    return False
                if l == 'A':
                    return True
                return accept(l, part)
"""
sol = 0
for part in parts:
    x,m,a,s = [int(x[2:]) for x in part[1:-1].split(',')]
    print(x,m,a,s)
    print(accept('in', {'x':x, 'm':m, 'a':a, 's':s}))
    if accept('in', {'x':x, 'm':m, 'a':a, 's':s}):
        sol += x + m + a + s
print(sol)
exit()
"""
regions = {c: [] for c in 'xmas'}
for wf in wfs:
    for rule in wfs[wf]:
        if rule['isCompare']:
            n = rule['n']
            for c in 'xmas':
                if c != rule['a']: continue
                regions[c].append(n)
                if rule['c'] == '<': regions[c].append(n-1)
                if rule['c'] == '>': regions[c].append(n+1)
print([(x, len(regions[x])) for x in 'xmas'])

for x in 'xmas':
    regions[x] = sorted(list(set(regions[x])) + [4000])
print(regions['x'])

"""
for x in range(1, 4001):
    for m in range(1, 4001):
        s = 0
        for a in range(1, 4001):
            s += sum([1 for s in range(1, 4001) if accept('in', {'x':x, 'm':m, 'a':a, 's':s})])
        print(x,m,s)
"""
sol_x = 0
for i, x in enumerate(regions['x']):
    sol_m = 0
    for ii, m in enumerate(regions['m']):
        sol_a = 0
        start = time.time()
        for iii, a in enumerate(regions['a']):
            sol_s = 0
            for iv, s in enumerate(regions['s']):
                if accept('in', {'x':x, 'm':m, 'a':a, 's':s}):
                    sol_s += (s - (regions['s'][iv-1] if iv > 0 else 0))
            #print(a, sol_s)
            sol_a += sol_s * (a - (regions['a'][iii-1] if iii > 0 else 0))
        end = time.time()
        print(x,m, sol_a, end-start)
        sol_m += sol_a * (m - (regions['m'][ii-1] if ii > 0 else 0))
    print(x, sol_m)
    sol_x += sol_m * (x - (regions['x'][i-1] if i > 0 else 0))
print(sol_x)

exit()
for x in range(1, 4001):
    for m in range(1, 4001):
        print(x,m)
        g = Grid([[1 if accept('in', {'x':x, 'm':m, 'a':a+1, 's':s+1}) else 0 for s in range(4000)] for a in range(4000)])
        g.save_image({1: (92, 131, 116), 0: (9, 38, 53)})
        print(g.count(1))
exit()

#1 1
#7244388
#6825214
#1 2
#7244388
#1 3
#7244388
#1 4
#1 1 1 2107
#1 1 143 1968
#1 1 172 2158

#167409079868000
#167409079868000
#167409079868000

"""
1 1 7244388 2.8054826259613037
1 170 7244388 2.5780937671661377
1 171 7244388 2.5661251544952393
1 176 7244388 2.5541574954986572
1 177 7244388 2.5681216716766357
"""