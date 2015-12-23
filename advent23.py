"""
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
"""
def b(a):
	b=0
	while a != 1:
		b+=1
		if a%2:
			a*=3
			a+=1
		else:
			a//=2
	return b

a =0
a+=1
a*=3
a+=1
a*=3
a+=1
a*=3
a*=3
a+=1
a+=1
a*=3
a*=3
a+=1
a+=1
a*=3
a+=1
a+=1
a*=3
print("Part 1:", a, b(a))
a =1
a*=3
a*=3
a+=1
a+=1
a*=3
a+=1
a+=1
a*=3
a+=1
a*=3
a+=1
a*=3
a+=1
a*=3
a+=1
a+=1
a*=3
a+=1
a+=1
a*=3
a*=3
a+=1
print("Part 2:", a, b(a))
