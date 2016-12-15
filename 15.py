discs = [(17,5),(19,8),(7,1),(13,7),(5,1),(3,0),(11,0)]
st = 0
while True:
    t = st
    for p,s in discs:
        t += 1
        if (s+t)%p: break
    else: break
    st += 1
print(st)
