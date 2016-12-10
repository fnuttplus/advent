class Bot:
    value = 0
    outhigh = False
    outlow = False

    def __init__(self,high,low,number):
        self.high = high
        self.low = low
        self.number = number

    def give(self,value):
        if self.value is 0: self.value = value
        else:
            if value > self.value: self.value, value = value, self.value

            if self.value is 61 and value is 17: print(self.number)

            if self.outhigh: output[self.high] = self.value
            else: bots[self.high].give(self.value)

            if self.outlow: output[self.low] = value
            else: bots[self.low].give(value)

bots = {}
output = {}

from sys import stdin
lines = sorted(stdin.read().splitlines())
for l in lines:
    l = l.split()
    if l[0] == "value":
        bots[l[5]].give(int(l[1]))
    elif l[0] == "bot":
        bots[l[1]] = Bot(l[11], l[6], l[1])
        if l[5] == 'output':
            bots[l[1]].outlow = True
        if l[10] == 'output':
            bots[l[1]].outhigh = True

print(output['0']*output['1']*output['2'])
