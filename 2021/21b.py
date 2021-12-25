from sys import stdin

lines = stdin.read().splitlines()

dice = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

memo = {}
def rec(pos, score, universes, turn):
    if (pos,score,universes,turn) in memo:
        return memo[(pos,score,universes,turn)]
    tu = [0,0]
    for d in dice:
        p = pos[turn]
        s = score[turn]

        p = (p + d) % 10
        s += 10 if p == 0 else p
        if s >= 21:
            tu[turn] += universes*dice[d]
        else:
            if turn == 0:
                tu1, tu2 = rec((p, pos[1]), (s, score[1]), universes*dice[d], 1)
            else:
                tu1, tu2 = rec((pos[0], p), (score[0], s), universes*dice[d], 0)
            tu[0] += tu1
            tu[1] += tu2

    memo[(pos,score,universes,turn)] = tu
    return tu

print(max(rec((4,2), (0,0), 1, 0)))
