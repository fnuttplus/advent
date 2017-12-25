gena = 883
genb = 879

i = 0
for _ in range(5000000):
	gena = (gena * 16807) % 2147483647
	while gena & 3 != 0:
		gena = (gena * 16807) % 2147483647
	genb = (genb * 48271) % 2147483647
	while genb & 7 != 0:
		genb = (genb * 48271) % 2147483647
	
	#print(bin(gena)[-16:].zfill(16), bin(genb)[-16:].zfill(16))

	if (gena & ((1<<16)-1) == genb & ((1<<16)-1)):
		i += 1

print(i)
