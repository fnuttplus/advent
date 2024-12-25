from sys import stdin
from aocd import get_data, submit
from re import findall

# https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        # Initialize swapped to track if any swaps occur
        swapped = False
        # Inner loop to compare adjacent elements
        for i in range(n):
            if ll[i + 1] in r and ll[i] in r[ll[i + 1]]:
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Mark that a swap has occurred
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

ls = stdin.read().split('\n\n')
r = {}
for l in ls[0].split('\n'):
    a,b = map(int,l.split('|'))
    if a in r:
        r[a].append(b)
    else:
        r[a] = [b]

s = 0
for l in ls[1].split('\n'):
    ll = list(map(int,l.split(',')))
    yay = True
    for a in range(len(ll)-1):
        for b in range(a, len(ll)):
            if ll[b] in r and ll[a] in r[ll[b]]:
                yay = False
    if not yay:
        bubble_sort(ll)
        s += ll[len(ll)//2]
        #print(ll, ll[len(ll)//2])

#print(r)
print(s)
