ins = list(map(int, input().split(','))) + [0]*2000

i = [2]

def val(*l):
    d = 10
    for a in l:
        d *= 10
        if (ins[ip]//d)%10 == 0:
            yield ins[a] 
        elif (ins[ip]//d)%10 == 1:
            yield a
        elif (ins[ip]//d)%10 == 2:
            yield ins[a+rbase]

rbase = 0
ip = 0
while ip < len(ins):
    op = ins[ip] % 100
    a, b, c = [ins[i] if i < len(ins) else 0 for i in range(ip+1, ip+4)]
    if (ins[ip]//10000)%10 == 2: c += rbase
    if op == 1:
        a, b = val(a,b)
        ins[c] = a + b
        ip += 4
    elif op == 2:
        a, b = val(a,b)
        ins[c] = a * b
        ip += 4
    elif op == 3:
        if (ins[ip]//100)%10 == 2: a += rbase
        ins[a] = i.pop()
        ip += 2
    elif op == 4:
        a, = val(a)
        print(a)
        ip += 2
    elif op == 5:
        a, b = val(a,b)
        if a != 0: ip = b
        else: ip += 3
    elif op == 6:
        a, b = val(a,b)
        if a == 0: ip = b
        else: ip += 3
    elif op == 7:
        a, b = val(a,b)
        if a < b: ins[c] = 1
        else: ins[c] = 0
        ip += 4
    elif op == 8:
        a, b = val(a,b)
        if a == b: ins[c] = 1
        else: ins[c] = 0
        ip += 4
    elif op == 9:
        a, = val(a)
        rbase += a
        ip += 2
    elif op == 99:
        break
    else:
        print("err")
    
