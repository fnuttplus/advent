from sys import stdin

data = stdin.read().splitlines()
particles = []
m = 1000
i = 0
for row in data:
    dp = row.split(', ')
    p,v,a = [list(map(int, dp[i][3:-1].split(','))) for i in range(3)]
    particles.append({'p':p, 'v':v, 'a':a, })
    d = sum(map(abs, a))
    if d < m:
        print(i, d)
        m = d
    i += 1

def cd(p1, p2): #collision detection
    return p1['p'][0] == p2['p'][0] and p1['p'][1] == p2['p'][1] and p1['p'][2] == p2['p'][2]

def dist(p):
    return sum(map(abs, p['p']))

collided = set()
for t in range(39):
    c = set()
    for i in range(len(particles)):
        if i in collided: continue
        particle = particles[i]
        particle['v'][0] += particle['a'][0]
        particle['v'][1] += particle['a'][1]
        particle['v'][2] += particle['a'][2]
        particle['p'][0] += particle['v'][0]
        particle['p'][1] += particle['v'][1]
        particle['p'][2] += particle['v'][2]
        for j in range(i):
            if j in collided: continue
            if cd(particle, particles[j]):
                c.add(i)
                c.add(j)
#                print(t, i, j, particle, particles[j])
    collided |= c
#    print(len(particles) - len(collided))

"""
m = 1000000
for i in range(len(particles)):
    d = dist(particles[i])
    if d < m:
        print(d, i)
        m = d
"""
print(len(particles) - len(collided))