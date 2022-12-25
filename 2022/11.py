from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

#ll = stdin.read().splitlines()
#ll = get_data(day=11).splitlines()

monkey_items = [
    [79, 98],
    [54, 65, 75, 74],
    [79, 60, 97],
    [74],
]
monkey_business = [0,0,0,0]
monkey_items = [
    [71, 86],
    [66, 50, 90, 53, 88, 85],
    [97, 54, 89, 62, 84, 80, 63],
    [82, 97, 56, 92],
    [50, 99, 67, 61, 86],
    [61, 66, 72, 55, 64, 53, 72, 63],
    [59, 79, 63],
    [55],
]
monkey_business = [0,0,0,0,0,0,0,0]

for _ in range(10000):
    """
    for m in range(4):
        for item in monkey_items[m]:
            monkey_business[m] += 1
            if m == 0:
                item = item * 19
                item //= 3
                if item % 23 == 0:
                    monkey_items[2].append(item)
                else:
                    monkey_items[3].append(item)
            if m == 1:
                item = item + 6
                item //= 3
                if item % 19 == 0:
                    monkey_items[2].append(item)
                else:
                    monkey_items[0].append(item)
            if m == 2:
                item = item * item
                item //= 3
                if item % 13 == 0:
                    monkey_items[1].append(item)
                else:
                    monkey_items[3].append(item)
            if m == 3:
                item = item + 3
                item //= 3
                if item % 17 == 0:
                    monkey_items[0].append(item)
                else:
                    monkey_items[1].append(item)
        monkey_items[m] = []
    print(monkey_items)
    """
    for m in range(8):
        for item in monkey_items[m]:
            monkey_business[m] += 1
            if m == 0:
                item = item * 13
                item = item % 9699690
                if item % 19 == 0:
                    monkey_items[6].append(item)
                else:
                    monkey_items[7].append(item)
            if m == 1:
                item = item + 3
                item = item % 9699690
                if item % 2 == 0:
                    monkey_items[5].append(item)
                else:
                    monkey_items[4].append(item)
            if m == 2:
                item = item + 6
                item = item % 9699690
                if item % 13 == 0:
                    monkey_items[4].append(item)
                else:
                    monkey_items[1].append(item)
            if m == 3:
                item = item + 2
                item = item % 9699690
                if item % 5 == 0:
                    monkey_items[6].append(item)
                else:
                    monkey_items[0].append(item)
            if m == 4:
                item = item * item
                item = item % 9699690
                if item % 7 == 0:
                    monkey_items[5].append(item)
                else:
                    monkey_items[3].append(item)
            if m == 5:
                item = item + 4
                item = item % 9699690
                if item % 11 == 0:
                    monkey_items[3].append(item)
                else:
                    monkey_items[0].append(item)
            if m == 6:
                item = item * 7
                item = item % 9699690
                if item % 17 == 0:
                    monkey_items[2].append(item)
                else:
                    monkey_items[7].append(item)
            if m == 7:
                item = item + 7
                item = item % 9699690
                if item % 3 == 0:
                    monkey_items[2].append(item)
                else:
                    monkey_items[1].append(item)
        monkey_items[m] = []
    #print(monkey_items)
#print(monkey_business)
#print(2*3*5*7*11*13*17*19)
print(145312*145314)
