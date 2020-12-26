from sys import stdin
il = [int(l) for l in stdin.read().splitlines()]

for i,a in enumerate(il):
    for j,b in enumerate(il[i+1:]):
        if a+b == 2020:
            print("PART 1:", a,b, a*b)
        for k,c in enumerate(il[i+j+1:]):
            if a+b+c == 2020:
                print("PART 2:", a,b,c, a*b*c)
