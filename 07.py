n = 0
while True:
    try: line = input()
    except: break
    br = False
    b1,a2 = line[:2]
    i = 2
    mibr = set()
    mobr = set()
    while i < len(line):
        if line[i] in '[]':
            br = (line[i] is '[')
            b1,a2 = line[i+1:i+3]
            i += 3
        a1,b1,a2 = b1,a2,line[i]
        if a1 == a2 and a1 != b1:
            if br: mibr.add(b1+a1)
            else: mobr.add(a1+b1)
        i += 1
    if mobr & mibr:
#        print(line)
#        print(mobr,mibr)
        n+=1
print(n)
