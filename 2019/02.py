ins0 = list(map(int, input().split(',')))

for x in range (100):
    for y in range(100):
        ins = ins0[:]
        ins[1] = x
        ins[2] = y
        ip = 0
        while ip < len(ins):
            op = ins[ip]
            if op == 1:
                ins[ins[ip+3]] = ins[ins[ip+1]] + ins[ins[ip+2]]
            elif op == 2:
                ins[ins[ip+3]] = ins[ins[ip+1]] * ins[ins[ip+2]]
            elif op == 99:
                break
            else:
                print("err")
            
            ip += 4

        if ins[0] == 19690720:
            print(100*x+y)
