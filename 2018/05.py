bp = list(input())

ab = "abcdefghijklmnopqrstuvwxyz"
AB = "abcdefghijklmnopqrstuvwxyz".upper()

for a in ab:
    p = list(filter(lambda x: x != a and x != a.upper(), bp))
    Done = False
    while not Done:
        Done = True
        i = 1
        while i < len(p):
            if (p[i] in ab and p[i-1] == p[i].upper()) or (p[i] in AB and p[i-1] == p[i].lower()):
                p = p[:i-1] + p[i+1:]
                Done = False
            else:
                i += 1
    print(a, len(p))
