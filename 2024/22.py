from sys import stdin
from aocd import get_data, submit, puzzle
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *
from oklab import viridis

s = 0
t = True
t = False

ls = puzzle.examples[0].input_data if t else get_data()
#ls = stdin.read() if t else get_data()

memo = {}

"""
    1. Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    2. Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    3. Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.

    To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
"""
ls = list(map(int, ls.splitlines()))
#ls = [123]
#ls = [1,10,100,2024]
#ls = [1,2,3,2024]
sequences = []

def change(n):
    n = n ^ (n *64)
    n = n % 16777216

    n = n ^ (n // 32)
    n = n % 16777216

    n = n ^ (n * 2048)
    n = n % 16777216
    return n

winnings = []
for n in ls:
    if t: print(n)
    seq = []
    bananas = {}
    for i in range(2000):
        c = change(n)
        seq.append(c % 10 - n % 10)
        n = c

        if len(seq) >= 4:
            if not tuple(seq[-4:]) in bananas:
                bananas[tuple(seq[-4:])] = n % 10 # price

    #print(bananas)
    winnings.append(bananas)

def wins(seq):
    return sum([w[seq] for w in winnings if seq in w])

#find the sequense in bananas that result in the highest combined price in all of winnings
def find_best(bananas):
    if t: print('b', bananas)
    best = 0
    for seq in bananas:
        w = wins(seq)
        if w > best:
            print('w', w, seq)
            best = w
    return best


# combine all the sequences in winnings
print(len([seq for w in winnings for seq in w]))
s = find_best([seq for w in winnings for seq in w])

if t:
    print()
    print('answer:', s)
    for i, e in enumerate(puzzle.examples): print(i, e)
else:
    submit(s)
