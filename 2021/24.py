from sys import stdin

lines = stdin.read().splitlines()

def run(numbers):
    d = {'w': 0,'x': 0,'y': 0,'z': 0,}
    for line in lines:
        s = line.split(' ')
        i = s[0]
        if i == 'inp':
            a = s[1]
            d[a] = numbers.pop()
        elif i == 'add':
            a = s[1]
            b = s[2]
            if b in d: b = d[b]
            else: b = int(b)
            d[a] = d[a] + b
        elif i == 'mul':
            a = s[1]
            b = s[2]
            if b in d: b = d[b]
            else: b = int(b)
            d[a] = d[a] * b
        elif i == 'div':
            a = s[1]
            b = s[2]
            if b in d: b = d[b]
            else: b = int(b)
            d[a] = int(d[a] / b)
        elif i == 'mod':
            a = s[1]
            b = s[2]
            if b in d: b = d[b]
            else: b = int(b)
            d[a] = d[a] % b
        elif i == 'eql':
            a = s[1]
            b = s[2]
            if b in d: b = d[b]
            else: b = int(b)
            d[a] = 1 if d[a] == b else 0
        else:break
    return d['z']
    
def run2(n):
    w,x,y,z = 0,0,0,0
    i = 14

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 + 11
    z = int(z/1)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 8) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 + 12
    z = int(z/1)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 8) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 + 10
    z = int(z/1)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 12) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 -8
    z = int(z/26)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 10) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 +15
    z = int(z/1)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 2) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 +15
    z = int(z/1)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 8) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 -11
    z = int(z/26)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 4) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 +10
    z = int(z/1)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 9) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 -3
    z = int(z/26)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 10) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 +15
    z = int(z/1)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 3) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 -3
    z = int(z/26)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 7) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 -1
    z = int(z/26)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 7) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 -10
    z = int(z/26)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 2) * x
    z += y

    i -= 1
    w = (n // 10**i) % 10
    x = z % 26 -16
    z = int(z/26)
    x = 0 if x == w else 1
    y = 25*x+1
    z *= y
    y = (w + 2) * x
    z += y

    return z

print(run([1,3,5,7,9,2,4,6,8,9,9,9,9,9]))
print(run2(99999864297531))

print(run2(99598963999971))
print(run2(93151411711211))
