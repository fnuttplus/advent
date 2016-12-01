from re import finditer
#from random import shuffle

lines = open("advent19.txt",'r').readlines()

replace = []
for replacements in lines[:-2]:
	r = replacements.split()
	replace.append((r[0], r[2]))

mol = lines[-1]
molecules = set()

for r in replace:
	rem = finditer(r[0],mol)
	for m in rem:
		molecules.add(mol[:m.span()[0]] + r[1] + mol[m.span()[1]:])

print(len(molecules))

#PART 2:

#replace.sort(key=lambda t: len(t[1]), reverse=True)
#shuffle(replace)
# A good order:
replace = [('P', 'PTi'), ('P', 'SiRnFAr'), ('Ca', 'PB'), ('Th', 'ThCa'), ('H', 'CRnFYMgAr'), ('O', 'NRnFAr'), ('Si', 'CaSi'), ('Ca', 'CaCa'), ('O', 'OTi'), ('N', 'HSi'), ('H', 'HCa'), ('H', 'ORnFAr'), ('Ca', 'SiRnMgAr'), ('F', 'PMg'), ('F', 'SiAl'), ('H', 'CRnAlAr'), ('O', 'CRnFYFAr'), ('Ti', 'BP'), ('O', 'HP'), ('H', 'NRnMgAr'), ('B', 'BCa'), ('F', 'CaF'), ('H', 'CRnFYFYFAr'), ('e', 'OMg'), ('Al', 'ThF'), ('e', 'HF'), ('e', 'NAl'), ('N', 'CRnFAr'), ('Mg', 'TiMg'), ('B', 'TiRnFAr'), ('H', 'NRnFYFAr'), ('Ca', 'PRnFAr'), ('Ti', 'TiTi'), ('H', 'CRnMgYFAr'), ('Ca', 'SiTh'), ('P', 'CaP'), ('H', 'OB'), ('O', 'CRnMgAr'), ('H', 'NTh'), ('Al', 'ThRnFAr'), ('B', 'TiB'), ('Mg', 'BF'), ('Ca', 'SiRnFYFAr')]
#print(replace)

#replace = [("O","HH"),("H","OH"),("H","HO"),("e","O"),("e","H")]
#shuffle(replace)
#mol = "HOHOHO"

stucks = set()
#unfoldables = set()

#def is_foldable(mol):
#	if mol in unfoldables: return False
#	for r in replace:
#		if mol in r[1]:
#			return True
#	unfoldables.add(mol)
#	return False

def fold(mol, n, path):
#	print(n, mol)
	for r in replace:
		for m in finditer(r[1], mol):
			mm = mol[:m.span()[0]] + r[0] + mol[m.span()[1]:]
			if mm in stucks:
				continue
			if mm == "e":
#				print(path)
				print(n)
				exit()
# not needed if lucky with input:
#			foldable = False
#			if m.span()[0] > 0:
#				if is_foldable(mol[m.span()[0]-1] if m.span()[0]==1 or mol[m.span()[0]-1].isupper() else mol[m.span()[0]-2:m.span()[0]] + r[0]):
#					foldable = True
#			if not foldable and m.span()[1] < len(mol):
#				if is_foldable(r[0] + mol[m.span()[1]] if m.span()[1]==len(mol)-1 or mol[m.span()[1]+1].isupper() else mol[m.span()[1]:m.span()[1]+2]):
#					foldable = True
#			if foldable or (m.span()[0] == 0 and m.span()[1] == len(mol)):
			fold(mm, n+1, path+[r[1]])

	stucks.add(mol)
#	print(len(stucks), mol)

fold(mol, 1,[])
