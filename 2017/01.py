s = input()
ii = 0
for i in range(len(s)):
	if s[i] == s[(i+len(s)//2) % len(s)]:
		ii += int(s[i])
print(ii)

