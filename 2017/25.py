tape = [0] * 7039
state = 'A'
pos = 7010

blueprint = {
    'A':((1, +1, 'B'),(0, -1, 'E')),
    'B':((1, -1, 'C'),(0, +1, 'A')),
    'C':((1, -1, 'D'),(0, +1, 'C')),
    'D':((1, -1, 'E'),(0, -1, 'F')),
    'E':((1, -1, 'A'),(1, -1, 'C')),
    'F':((1, -1, 'E'),(1, +1, 'A'))
}

for x in range(12386363):
    a,b,c = blueprint[state][tape[pos]]
    tape[pos] = a
    pos += b
    state = c

print(tape.count(1))
