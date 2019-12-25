from threading import Thread
from queue import Queue

class Computer:
    def mod(self, c, a, b=1):
        for i in range(a, a+b):
            self.ins[i] = c

    def get(self):
        while True:
            q = self.outq.get()
            if q is None: break
            yield q

    def start(self):
        Thread(target=self.run).start()

    def __init__(self, instructions, debug=False):
        self.debug = debug
        self.ins = {i: val for i, val in enumerate(list(map(int, instructions.split(','))))}
        self.ip, self.rbase = 0, 0
        self.inq, self.outq = Queue(), Queue()

    def val(self, a, d):
        m = (self.ins[self.ip]//d)%10
        if m == 0: return self.ins[a] if a in self.ins else 0
        elif m == 1: return a
        elif m == 2: return self.ins[a+self.rbase] if a+self.rbase in self.ins else 0

    def run(self):
        while True:
            op = self.ins[self.ip] % 100
            aw, b, c = [self.ins[i] if i in self.ins else 0 for i in range(self.ip+1, self.ip+4)]
            a = self.val(aw, 100)
            b = self.val(b, 1000)
            if (self.ins[self.ip]//100)%10 == 2: aw += self.rbase
            if (self.ins[self.ip]//10000)%10 == 2: c += self.rbase
            if op == 0:
                if self.debug: print("%d. nop" %(self.ip))
                self.ip += 1
            elif op == 1:
                if self.debug: print("%d. ins[%d] = %d + %d" %(self.ip, c, a, b))
                self.ins[c] = a + b
                self.ip += 4
            elif op == 2:
                if self.debug: print("%d. ins[%d] = %d * %d" %(self.ip, c, a, b))
                self.ins[c] = a * b
                self.ip += 4
            elif op == 3:
                self.ins[aw] = self.inq.get()
                if self.debug: print("%d.in ins[%d] = %d" %(self.ip, aw, self.ins[aw]))
                self.ip += 2
            elif op == 4:
                if self.debug: print("%d. out(%d), %d" %(self.ip, a, aw))
                self.outq.put(a)
                self.ip += 2
            elif op == 5:
                if self.debug: print("%d. %d != 0: ip=%d" %(self.ip, a, b))
                if a != 0: self.ip = b
                else: self.ip += 3
            elif op == 6:
                if self.debug: print("%d. %d == 0: ip=%d" %(self.ip, a, b))
                if a == 0: self.ip = b
                else: self.ip += 3
            elif op == 7:
                if self.debug: print("%d. %d < %d: ins[%d]=1" %(self.ip, a, b, c))
                if a < b: self.ins[c] = 1
                else: self.ins[c] = 0
                self.ip += 4
            elif op == 8:
                if self.debug: print("%d. %d == %d: ins[%d]=1" %(self.ip, a, b, c))
                if a == b: self.ins[c] = 1
                else: self.ins[c] = 0
                self.ip += 4
            elif op == 9:
                if self.debug: print("%d. rbase += %d" %(self.ip, a))
                self.rbase += a
                self.ip += 2
            elif op == 99:
                self.outq.put(None)
                break
            else:
                print("err", op)
