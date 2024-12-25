from sys import stdin
from aocd import get_data, submit, puzzle
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *
from oklab import viridis
from math import prod
import networkx as nx
import matplotlib.pyplot as plt
from schemdraw.parsing import logicparse

s = 0
t = True
t = False

#ls = puzzle.examples[0].input_data if t else get_data()
ls = stdin.read() if t else get_data()

memo = {}

wire_values = {}
gates = {}
wires = set()
for l in ls.split('\n\n')[0].splitlines():
    a,b = l.split(': ')
    wire_values[a] = b
    wires.add(a)

for l in ls.split('\n\n')[1].splitlines():
    a,b = l.split(' -> ')
    x,y,z = a.split(' ')
    gates[b] = (x, y, z)
    wires.add(b)

def get_value(wire):
    if wire in wire_values:
        return int(wire_values[wire])
    else:
        x, y, z = gates[wire]
        if x == 'NOT':
            return ~get_value(y)
        elif y == 'AND':
            return get_value(x) & get_value(z)
        elif y == 'OR':
            return get_value(x) | get_value(z)
        elif y == 'XOR':
            return get_value(x) ^ get_value(z)
        else:
            return get_value(y)

for wire in sorted(list(wires)):
    if wire.startswith('z'):
        bit = int(wire[1:])
        s += (get_value(wire) << bit)
print(s)

#convert wires and gates to an expression for logicparse
def to_expr(wire, depth):
    if wire in wire_values or depth == 0:
        return wire
    else:
        x, y, z = gates[wire]
        return f'({to_expr(x, depth-1)} {y.lower()} {to_expr(z, depth-1)})'

with logicparse(to_expr('z06', 100), outlabel='$z06$') as d: d.save(f'circuit_z06.svg')

# determine if two expression trees are equivalent
def equivalent(a, b):
    if a == "?" or b == "?": return True

    if type(a) == str:
        if not a in gates: return False
        a = gates[a]
    if type(b) == str:
        if not b in gates: return False
        b = gates[b]

    a1, a_op, a2 = a
    b1, b_op, b2 = b
    if a_op != b_op:
        return False
    if a1 in wire_values and a2 in wire_values:
        return (a1 == b1 or a1 == b2) and (a2 == b1 or a2 == b2)

    return equivalent(a1, b1) and equivalent(a2, b2) or equivalent(a1, b2) and equivalent(a2, b1)

gates['vdk'], gates['mmf'] = gates['mmf'], gates['vdk']
gates['dpg'], gates['z25'] = gates['z25'], gates['dpg']
gates['tvp'], gates['z15'] = gates['z15'], gates['tvp']
gates['kmb'], gates['z10'] = gates['z10'], gates['kmb']

for i in range(2, 45):
    if not equivalent(f'z{i:02}', ((f'y{i:02}', 'XOR', f'x{i:02}'), 'XOR', (('?', 'AND', '?'), 'OR', (f'y{i-1:02}', 'AND', f'x{i-1:02}')))):
        print('error: ', f'z{i:02}', to_expr(f'z{i:02}', 3))
        print(((f'y{i:02}', 'XOR', f'x{i:02}'), 'XOR', (('?', 'AND', '?'), 'OR', (f'y{i-1:02}', 'AND', f'x{i-1:02}'))))

print(','.join(sorted(['vdk', 'mmf', 'dpg', 'z25', 'tvp', 'z15', 'kmb', 'z10'])))


#fsh OR jkh -> z15
#y25 AND x25 -> z25
#vrn AND dkr -> z10

#y35 XOR x35 -> vdk
#x35 AND y35 -> mmf

#bpw XOR dgv -> dpg
#y25 AND x25 -> z25

#vrn XOR dkr -> kmb
#vrn AND dkr -> z10

#kvg XOR qts -> tvp
#fsh OR jkh -> z15


"""
z10: ((x10 xor y10) *and (psh or qrc))
z15: ((y15 *and x15) *or (qts *and kvg))
z16: ((kvg *xor qts) xor (y16 xor x16))
z25: (y25 *and x25)
z35: ( (x35 *and y35) xor (gbs or nvt))

error:  z10 ((x10 xor y10) and ((vsm and bnj) or (x09 and y09)))
(('y10', 'XOR', 'x10'), 'XOR', (('?', 'AND', '?'), 'OR', ('y09', 'AND', 'x09')))
error:  z11 ((x11 xor y11) xor ((y10 and x10) or (vrn xor dkr)))
(('y11', 'XOR', 'x11'), 'XOR', (('?', 'AND', '?'), 'OR', ('y10', 'AND', 'x10')))

error:  z15 ((y15 and x15) or ((sjm or dcr) and (x15 xor y15)))
(('y15', 'XOR', 'x15'), 'XOR', (('?', 'AND', '?'), 'OR', ('y14', 'AND', 'x14')))
error:  z16 (((x15 xor y15) xor (sjm or dcr)) xor (y16 xor x16))
(('y16', 'XOR', 'x16'), 'XOR', (('?', 'AND', '?'), 'OR', ('y15', 'AND', 'x15')))

error:  z25 (y25 and x25)
(('y25', 'XOR', 'x25'), 'XOR', (('?', 'AND', '?'), 'OR', ('y24', 'AND', 'x24')))
error:  z26 (((bpw xor dgv) or (dgv and bpw)) xor (x26 xor y26))
(('y26', 'XOR', 'x26'), 'XOR', (('?', 'AND', '?'), 'OR', ('y25', 'AND', 'x25')))

error:  z35 ((x35 and y35) xor ((x34 and y34) or (sjd and qjg)))
(('y35', 'XOR', 'x35'), 'XOR', (('?', 'AND', '?'), 'OR', ('y34', 'AND', 'x34')))
error:  z36 (((mmf and tsw) or (y35 xor x35)) xor (y36 xor x36))
(('y36', 'XOR', 'x36'), 'XOR', (('?', 'AND', '?'), 'OR', ('y35', 'AND', 'x35')))
"""


if t:
    print()
    print('answer:', s)
    for i, e in enumerate(puzzle.examples): print(i, e)
else:
    print(s)
