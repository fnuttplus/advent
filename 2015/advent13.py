from itertools import permutations as perm

happiness = [
("Alice", +54, "Bob"),("Alice", -81, "Carol"),("Alice", -42, "David"),("Alice", +89, "Eric"),("Alice", -89, "Frank"),("Alice", +97, "George"),("Alice", -94, "Mallory"),
("Bob", +3, "Alice"),("Bob", -70, "Carol"),("Bob", -31, "David"),("Bob", +72, "Eric"),("Bob", -25, "Frank"),("Bob", -95, "George"),("Bob", +11, "Mallory"),
("Carol", -83, "Alice"),("Carol", +8, "Bob"),("Carol", +35, "David"),("Carol", +10, "Eric"),("Carol", +61, "Frank"),("Carol", +10, "George"),("Carol", +29, "Mallory"),
("David", +67, "Alice"),("David", +25, "Bob"),("David", +48, "Carol"),("David", -65, "Eric"),("David", +8, "Frank"),("David", +84, "George"),("David", +9, "Mallory"),
("Eric", -51, "Alice"),("Eric", -39, "Bob"),("Eric", +84, "Carol"),("Eric", -98, "David"),("Eric", -20, "Frank"),("Eric", -6, "George"),("Eric", +60, "Mallory"),
("Frank", +51, "Alice"),("Frank", +79, "Bob"),("Frank", +88, "Carol"),("Frank", +33, "David"),("Frank", +43, "Eric"),("Frank", +77, "George"),("Frank", -3, "Mallory"),
("George", -14, "Alice"),("George", -12, "Bob"),("George", -52, "Carol"),("George", +14, "David"),("George", -62, "Eric"),("George", -18, "Frank"),("George", -17, "Mallory"),
("Mallory", -36, "Alice"),("Mallory", +76, "Bob"),("Mallory", -34, "Carol"),("Mallory", +37, "David"),("Mallory", +40, "Eric"),("Mallory", +18, "Frank"),("Mallory", +7, "George")]

guests = ["Alice","Bob","Carol","David","Eric","Frank","George","Mallory"]

def get_h(guest1, guest2):
	p = 0
	if guest1 == "fnuttplus" or guest2 == "fnuttplus": return 0
	for h in happiness:
		if (h[0] == guest1 and h[2] == guest2) or (h[0] == guest2 and h[2] == guest1):
			p += h[1]
	return p

maxh = 0
#brute force 40320 permutations
for p in perm(guests):
	h = 0
	guest1 = "fnuttplus"
	for guest2 in p:
		h+=get_h(guest1,guest2)
		guest1 = guest2
	if maxh < h:
		maxh = h
		print("fnuttplus", p, h)
print(maxh)
#part 1: 709
#part 2: 668
