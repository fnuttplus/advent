def length(s):
    i = 0
    n = 0
    while i < len(s):
        if s[i] is '(':
            c = s.find(')',i)+1
            a,b = map(int, s[i+1:c-1].split('x'))
            i = c+a
#            a = length(s[c:i])
            n+=a*b
        else:
            i+=1
            n+=1
    return n

print(length(input()))
