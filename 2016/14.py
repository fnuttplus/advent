from hashlib import md5

def findtriplet(h):
    a,b = h[:2]
    for c in h[2:]:
        if a==b==c:
            return a
        a,b = b,c
    return False

triplets = [('t',0)]
keys = []
i = -1
d = 0
while len(keys)<75:
    i+=1
    h = "zpqevtbw"+str(i)
    for _ in range(1):
        h = md5(h.encode()).hexdigest()
    a = findtriplet(h)
    if triplets[0][1] < i-1000:
        triplets.pop(0)
    if a:
        d += len(triplets)
        for t in triplets:
            if t[0]*5 in h:
                keys.append(t[1])
        triplets.append((a,i))

print(d)
print(sorted(keys))
print(sorted(keys)[63])
