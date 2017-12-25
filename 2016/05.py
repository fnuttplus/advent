from hashlib import md5
from random import choice
from sys import stdin, stdout

i = 0
code = ['_']*8

while True:
    m = md5()
    m.update(("ojvtpuvg"+str(i)).encode())
    h = m.hexdigest()

    if i%10000 == 0:
        stdout.write(''.join([choice("0123456789abcdef") if c is '_' else c for c in code]))
        stdout.flush()
        stdout.write('\b'*8)

    if h[:5] == "00000":
        if h[5] in "01234567":
            if code[int(h[5])] == '_':
                code[int(h[5])] = h[6]
                if not '_' in code:
                    break
    i +=1

print(''.join(code))
#print(i) #27649592
