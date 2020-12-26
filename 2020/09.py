from sys import stdin

op = list(map(int, stdin.read().splitlines()))

def valid(i):
    for j in range(i - 25, len(op)):
        for k in range(j + 1, i):
            if op[j] + op[k] == op[i]:
                return True
    return False

for i in range(25, len(op)):
    if not valid(i): break

s = op[i]
print(s)
for j in range(2, 100):
    for i in range(len(op)):
        if s == sum(op[i:i+j]):
            #print(j, op[i:i+j])
            print(min(op[i:i+j]) + max(op[i:i+j]))
