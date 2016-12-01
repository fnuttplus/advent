from hashlib import md5

key = b"bgvyzdsv"
i = 0
while not md5(key+bytes(str(i),'ascii')).hexdigest()[:6] == "000000":
	i+=1
print(i)