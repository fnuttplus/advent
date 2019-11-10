from sys import stdin

pp = [[tuple(map(int, x.split(','))), []] for x in stdin.read().splitlines()]

def close(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3]) <= 3

for i in range(len(pp)):
    for j in range(i):
        if close(pp[i][0], pp[j][0]):
            pp[i][1].append(j)
            pp[j][1].append(i)

visited = [False] * len(pp)

def dfs(i):
    for p in pp[i][1]:
        if visited[p] == False:
            visited[p] = True
            dfs(p)

n = 0
for i in range(len(visited)):
    if not visited[i]:
        n += 1
        dfs(i)

print(n)
