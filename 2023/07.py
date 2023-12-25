from sys import stdin
from aocd import get_data, submit
from re import findall

#d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]

#grid = [list(x)+['.'] for x in stdin.read().splitlines()]

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
cards = list(reversed(cards))

def type(hand):
    v = {}
    for c in cards:
        v[c] = hand.count(c)
    j = v['J']
    del v['J']
    v = list(v.values())
    if 5 in v:
        return 7
    if 4 in v:
        if j == 1: return 7
        return 6
    if 3 in v and 2 in v:
        if j == 2 or j == 3: return 7
        return 5
    if 3 in v:
        if j == 2: return 7
        if j == 1: return 6
        return 4
    if v.count(2) == 2:
        if j == 1: return 5
        return 3
    if 2 in v:
        if j == 1: return 4
        if j == 2: return 6
        if j == 3: return 7
        return 2
    if j == 5: return 7
    if j == 4: return 7
    if j == 3: return 6
    if j == 2: return 4
    if j == 1: return 2
    return 1

hands = [x.split(' ') for x in stdin.read().splitlines()]

hands = sorted(hands, key=lambda hand: tuple([type(hand[0])] + [cards.index(c) for c in hand[0]]))

s = 0
for i, hand in enumerate(hands):
    s += (i+1) * int(hand[1])
    print(i+1, int(hand[1]), hand[0], tuple([type(hand[0])] + [cards.index(c) for c in hand[0]]))
print(s)
