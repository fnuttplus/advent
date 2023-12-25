from sys import stdin
from aocd import get_data, submit
from re import findall

#d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]

#grid = [list(x)+['.'] for x in stdin.read().splitlines()]

lines = stdin.read().split('\n\n')

seeds = [int(x) for x in lines[0].split(' ')[1:]]
print(seeds)
maps = [x.split('\n')[1:] for x in lines[1:]]

print(maps)

sol = 10**10
for i in range(0, len(seeds), 2):
    print(seeds[i],seeds[i+1])
    ranges = [(seeds[i],seeds[i+1])]

    for map in maps:
        print(map)
        overlaps = []
        for r in map:
            print(r)
            r = [int(x) for x in r.split(' ')]
            a,b,c = r
            noverlaps = []

            for i in range(len(ranges)):
                s, r = ranges[i]

                #bcccc
                #  srrrr
                if b <= s and s+r > b+c >= s:
                    overlaps.append((a + s-b, b+c-s))
                    noverlaps.append((b+c, r-(b+c-s)))
                #    b++++
                #  s----
                elif s < b and b+c > s+r >= b:
                    overlaps.append((a, s+r-b))
                    noverlaps.append((s, b-s))
                #   b++
                #  s----
                elif s < b and s+r >= b+c:
                    overlaps.append((a, c))
                    noverlaps.append((s, b-s))
                    if (s+r > b+c):
                        noverlaps.append((b+c, (s+r)-(b+c)))
                # b++++
                #  s--
                elif b <= s and s+r <= b+c:
                    overlaps.append((a + s-b, r))
                else:
                    noverlaps.append((s,r))

            ranges = noverlaps
            print(ranges, overlaps)
        ranges = overlaps + noverlaps

    print(ranges)
    if sol > min(x[0] for x in ranges):
        sol = min(x[0] for x in ranges)
print(sol)

exit()

s = 10**10
for i in range(0, len(seeds), 2):
    print(seeds[i],seeds[i+1])
    #ranges = [(seeds[i],seeds[i+1])]
    for seed in range(seeds[i], seeds[i]+seeds[i+1]):
        #print('===', seed, '===')
        for map in maps:
            for r in map:
                r = [int(x) for x in r.split(' ')]
            #    print(r)
                a,b,c = r
                if b <= seed <=b+c:
                    seed = a + (seed - b)
                    break
            #print(seed)
        if seed < s:
            s = seed
    print(s)

