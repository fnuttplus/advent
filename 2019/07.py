from itertools import permutations
ins0 = list(map(int, input().split(',')))

i = [0,1,2,3,4]

def val(*l):
    d = 10
    for a in l:
        d *= 10
        yield ins[a] if (ins[ip[j]]//d)%10 == 0 else a

m = 0
for p in permutations([5,6,7,8,9], 5):
    inss = [ins0[:] for _ in range(5)]
    il = [[pp] for pp in p]
    j = 0
    ins = inss[j]
    il[j].insert(0,0)
    i = il[j]
    ip = [0]*5
    while ip[j] < len(ins):
        op = ins[ip[j]] % 100
        a, b, c = [ins[i] if i < len(ins) else 0 for i in range(ip[j]+1, ip[j]+4)]
        if op == 1:
            a, b = val(a,b)
            ins[c] = a + b
            ip[j] += 4
        elif op == 2:
            a, b = val(a,b)
            ins[c] = a * b
            ip[j] += 4
        elif op == 3:
            ins[a] = i.pop()
            ip[j] += 2
        elif op == 4:
            a, = val(a)
            #print(a, j, i, il)
            x = a
            ip[j] += 2
            j = (j+1)%5
            ins = inss[j]
            il[j].insert(0, a)
            i = il[j]
        elif op == 5:
            a, b = val(a,b)
            if a != 0: ip[j] = b
            else: ip[j] += 3
        elif op == 6:
            a, b = val(a,b)
            if a == 0: ip[j] = b
            else: ip[j] += 3
        elif op == 7:
            a, b = val(a,b)
            if a < b: ins[c] = 1
            else: ins[c] = 0
            ip[j] += 4
        elif op == 8:
            a, b = val(a,b)
            if a == b: ins[c] = 1
            else: ins[c] = 0
            ip[j] += 4
        elif op == 99:
            break
        else:
            print("err")
    if x > m:
        m = x
        print(p, x)
