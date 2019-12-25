from vm import Computer

comp = Computer(input(), False)

comp.start()
"""
north
take festive hat
east
take prime number
west
west
take sand
south
north
east
south
east
north
take weather machine
north
take mug
south
south
east
!take photons
north
east
!take escape pod
east
take astronaut ice cream
west
west
south
west
west
south
south
take mutex
south
take boulder
east
!take giant electromagnet
south
inv
drop prime number
drop weather machine
drop mug
drop festive hat
inv
east
"""
for c in "north\nwest\ntake sand\neast\nsouth\neast\neast\nnorth\neast\neast\ntake astronaut ice cream\nwest\nwest\nsouth\nwest\nwest\nsouth\nsouth\ntake mutex\nsouth\ntake boulder\neast\nsouth\neast\n":
    comp.inq.put(ord(c))

for q in comp.get():
    print(chr(q),end="")

# weather machine     268435456
# mug                 134217728
# prime number        67108864
# sand                2097152
# astronaut ice cream 131072
# festive hat         16384
# mutex               8192
# boulder             256
