a, b = 0, 1
l = "37"

for i in range(54893402):
    if i % 1000000 == 0: print(i)
    l += str(int(l[a])+int(l[b]))
    a = (a + 1 + int(l[a])) % len(l)
    b = (b + 1 + int(l[b])) % len(l)

print(l.find("380621"))
print(l.find("59414"))
print(l.find("92510"))
