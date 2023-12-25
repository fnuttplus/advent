from sys import stdin
from re import findall
from aoc import Grid
import heapq
import time
from copy import deepcopy as copy

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
#print(wfs)

def prod(spans):
    return (spans['x'][1] - spans['x'][0] +1) * (spans['m'][1] - spans['m'][0] +1) * (spans['a'][1] - spans['a'][0] +1) * (spans['s'][1] - spans['s'][0] +1)

def parse(wf, spans):
    if wf == 'A':
        print(spans)
        return prod(spans)
    if wf == 'R':
        return 0
#    print(wf, spans)
    s = 0
    for rule in wfs[wf]:
#        print(rule)
        if not rule['isCompare']:
            s += parse(rule['next'], spans)
        else:
            a = False
            span1 = copy(spans)
            if rule['c'] == '>':
                span1[rule['a']][0] = rule['n'] + 1
                spans[rule['a']][1] = rule['n']
                s += parse(rule['next'], span1)
            elif rule['c'] == '<':
                span1[rule['a']][1] = rule['n'] - 1
                spans[rule['a']][0] = rule['n']
                s += parse(rule['next'], span1)
    return s

print(parse('in', {x: [1,4000] for x in 'xmas'}))
#167409079868000
