from sys import stdin

op = [line.split() for line in stdin.read().splitlines()]

def run():
    s = set()
    ip = 0
    acc = 0
    while True:
        if ip in s: return False, acc
        s.add(ip)
        if ip >= len(op): return True, acc
        ins, arg = op[ip]
        arg = int(arg)
        #print(ins, arg)
        if ins == 'nop':
            ip += 1
        elif ins == 'acc':
            acc += arg
            ip += 1
        elif ins == 'jmp':
            ip += arg

print(run()[1])

for i in range(len(op)):
    #print(i)
    if op[i][0] == 'nop':
        op[i][0] = 'jmp'
        a, b = run()
        if a:
            print(b)
            break
        op[i][0] = 'nop'

    elif op[i][0] == 'jmp':
        op[i][0] = 'nop'
        a, b = run()
        if a:
            print(b)
            break
        op[i][0] = 'jmp'
