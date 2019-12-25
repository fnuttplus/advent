j = 0
for p in range(264360, 746325):
    s = str(p)
    c0 = s[0]
    for c in s[1:]:
        if c < c0: break
        c0 = c
    else:
        for i in range(1,6):
            if s[i] == s[i-1]:
                if (i-2 < 0 or s[i-2] != s[i]) and (i+1 > 5 or s[i+1] != s[i]):
                    j += 1
                    print(p)
                    break

print(j)