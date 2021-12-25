#from aocd import lines, numbers, submit
from sys import stdin

numbers = [int(x) for x in stdin.read().splitlines()]
s = sum([1 if numbers[x] > numbers[x-1] else 0 for x in range(len(numbers))])
print(s)

#part 2
numbers = [sum(numbers[x:x+3]) for x in range(len(numbers)-2)]
s = sum([1 if numbers[x] > numbers[x-1] else 0 for x in range(len(numbers))])
print(s)
