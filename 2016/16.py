def next(a):
    b = ''
    for c in reversed(a):
        b += '0' if c is '1' else '1'
    return a+'0'+b

def chs(s):
    while len(s)&1 is 0:
        s1 = ''
        for i in range(0,len(s),2):
            a,b = s[i:i+2]
            s1 += '1' if a is b else '0'
        s = s1
    return s

a = "10001001100000001"
l = 35651584
while len(a) < l:
    a = next(a)
print(chs(a[:l]))
