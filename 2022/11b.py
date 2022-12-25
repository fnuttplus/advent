from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

#ll = stdin.read().split('\n\n')
ll = get_data(day=11).split('\n\n')
monkeys = []
for l in ll:
    m = l.splitlines()
    monkeys.append({
        'items': list(map(int, m[1].split(': ')[1].split(', '))),
        'operation': m[2].split('= ')[1],
        'test': int(m[3].split('y ')[1]),
        'true': int(m[4].split('y ')[1]),
        'false': int(m[5].split('y ')[1]),
        'business': 0
    })
print(monkeys)

for _ in range(10000):
    for m in range(len(monkeys)):
        for i in range(len(monkeys[m]['items'])):
            monkeys[m]['business'] += 1
            old = monkeys[m]['items'][i]
            item = eval(monkeys[m]['operation'])
            #item = item // 3
            item = item % 9699690
            if item % monkeys[m]['test'] == 0:
                monkeys[monkeys[m]['true']]['items'].append(item)
            else:
                monkeys[monkeys[m]['false']]['items'].append(item)

        monkeys[m]['items'] = []
    #print([m['items'] for m in monkeys])

ss = sorted([m['business'] for m in monkeys], reverse=True)[:2]
print(ss[0] * ss[1])
#print(ss)
#print(monkeys)
