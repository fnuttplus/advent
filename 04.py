n = 0
ab = "abcdefghijklmnopqrstuvwxyz"

while True:
    try: line = input()
    except: break

    f = sorted([(-line[:-11].count(a), a) for a in ab])[:5]
    ID = int(line[-10:-7])
    h = line[-6:-1]

    for i in range(5):
        if f[i][1] != h[i]: break
    else:
        room = ''.join([' ' if c is '-' else ab[(ab.index(c)+ID)%26] for c in line[:-11]])
        if "north" in room:
            print(room, ID)
        n += ID

print(n)
