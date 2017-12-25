s = [1 if c is '.' else 0 for c in input()]
l = len(s)
n = 0
for _ in range(40):
    print(''.join(['.' if c else '^' for c in s]))
    n += sum(s)
    s = [1]+s+[1]
    s = [s[i] == s[i+2] for i in range(l)]
print(n)
