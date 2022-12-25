from sys import stdin
from aocd import submit, get_data, lines

d = {}
s = get_data(day=7).splitlines()
#s = stdin.read().splitlines()
st = []
for line in s:
    a = line.split(' ')
    if a[0] == '$':
        if a[1] == 'cd':
            if a[2] == '..':
                st.pop()
            else:
                st.append(a[2])
        if a[1] == 'ls':
            d['/'.join(st)] = []
    else:
        d['/'.join(st)].append(a)
t = 0
m = 70000000
def dfs(cd):
    global t,m
    s = 0
    for dd in d[cd]:
        if dd[0] == 'dir':
            s += dfs(cd+'/'+dd[1])
        else:
            s += int(dd[0])
    if s <= 100000:
        t += s
    if s > 40358913 - 40000000:
        if s < m:
            m = s
    #print(cd, s)
    return s

dfs('/')
print(t)
print(m)
