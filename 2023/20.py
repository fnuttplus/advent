from sys import stdin
from re import findall
from aoc import Grid
import heapq
import time

#g = Grid().from_stdin()

lines = stdin.read().splitlines()
config = {}
class Module:
    def __init__(self, type, out):
        self.type = type
        self.out = out
    def __repr__(self):
        return f"{{ {self.type}, [{', '.join(self.out)}] }}"

for line in lines:
    n, o = line.split(' -> ')
    t = 'b'
    if n != 'broadcaster':
        t = n[0]
        n = n[1:]
    config[n] = Module(t, o.split(', '))
ffs = {}
cjs = {}
for c in config:
    m = config[c]
    if m.type == '%':
        ffs[c] = 0
    if m.type == '&':
        cjs[c] = {}
for c in config:
    m = config[c]
    for o in m.out:
        if o == 'rx': continue
        if config[o].type == '&':
            cjs[o][c] = 0

print(config)
print(cjs)

stack = []

lows = 0
highs = 0
rx = -1
def pulse(orig, signal, module):
    global lows
    global highs
    global rx
    if signal == 0: lows += 1
    if signal == 1: highs += 1
    #print(orig, '-low->' if signal == 0 else '-high->', module)
    if module == 'rx':
        rx = signal
        if rx == 0:
            print(i)
            exit()
        return
    m = config[module]
    if m.type == '%':
        if signal == 0:
            ffs[module] ^= 1
            signal = ffs[module]
        else: return
    if m.type == '&':
        if signal == 1 and module == 'cs': print(orig, i)
        cjs[module][orig] = signal
        signal = 1 if 0 in cjs[module].values() else 0
    for o in m.out:
        stack.append((module, signal, o))

def button():
    stack.append(('button', 0, 'broadcaster'))
    while stack: pulse(*stack.pop(0))


a = 61130883769
b = 59244613249
c = 58821113333
d = 57413979797

pl = 3768*a+a-1
sk = 3888*b+b-1
sd = 3916*c+c-1
zv = 4012*d+d-1

print(pl + 1)

for i in range(1000):
    button()
print(highs * lows)

for i in range(1000, 10000):
    button()

"""
230402300925361
703315117
pl 3768
sk 3888
sd 3916
zv 4012
pl 7537
sk 7777
sd 7833
zv 8025
"""
