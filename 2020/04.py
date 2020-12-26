from sys import stdin
import re

def isvalid(d):
    if 'byr' in d and 'iyr' in d and 'eyr' in d and 'hgt' in d and 'hcl' in d and 'ecl' in d and 'pid' in d:
        if not (1920 <= int(d['byr']) <= 2002): return False
        if not (2010 <= int(d['iyr']) <= 2020): return False
        if not (2020 <= int(d['eyr']) <= 2030): return False
        if d['hgt'][-2:] == 'cm':
            if not (150 <= int(d['hgt'][:-2]) <= 193): return False
        elif d['hgt'][-2:] == 'in':
            if not (59 <= int(d['hgt'][:-2]) <= 76): return False
        else: return False
        if not re.match(r'\#[0-9a-f]{6}', d['hcl']): return False
        if not d['ecl'] in ["amb","blu","brn","gry","grn","hzl","oth"]: return False
        if not (d['pid'].isnumeric() and len(d['pid']) == 9): return False

        return True
    return False

d = {}
i = 0
for line in stdin.read().splitlines():
    if line == "":
        if isvalid(d):
            i += 1
        d = {}
    else:
        for dd in line.split(' '):
            a,b = dd.split(':')
            d[a] = b
if isvalid(d):
    i += 1
print(i)