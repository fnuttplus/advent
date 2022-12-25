from sys import stdin
#from aocd import lines, submit
from math import prod

r = stdin.read().strip()
p = bin(int(r, 16))[2:].zfill(len(r)*4)
#print(p)

def ppc(pc, n):
    return int(p[pc:pc+n], 2), pc + n

s = 0
def parse(pc):
    global s
    ss = ''
    v, pc = ppc(pc, 3)
    t, pc = ppc(pc, 3)
    if t != 4:
        i, pc = ppc(pc, 1)
        sp = []
        sss = []
        if i == 0:
            l, pc = ppc(pc, 15)
            c = pc
            while pc - c < l:
                pc, a, s0 = parse(pc)
                sp.append(a)
                sss.append(s0)
        else:
            l, pc = ppc(pc, 11)
            for _ in range(l):
                pc, a, s0 = parse(pc)
                sp.append(a)
                sss.append(s0)
        if t == 0:
            pp = sum(sp)
            ss = '(' + ' + '.join(sss) + ')'
        elif t == 1:
            pp = prod(sp)
            ss = '(' + ' * '.join(sss) + ')'
        elif t == 2:
            pp = min(sp)
            ss = 'min([' + ', '.join(sss) + '])'
        elif t == 3:
            pp = max(sp)
            ss = 'max([' + ', '.join(sss) + '])'
        elif t == 5:
            pp = 1 if sp[0] > sp[1] else 0
            ss = '(' + sss[0] + ' > ' + sss[1] + ')'
        elif t == 6:
            pp = 1 if sp[0] < sp[1] else 0
            ss = '(' + sss[0] + ' < ' + sss[1] + ')'
        elif t == 7:
            pp = 1 if sp[0] == sp[1] else 0
            ss = '(' + sss[0] + ' == ' + sss[1] + ')'

    else:
        aa = ''
        while p[pc] != '0':
            aa += p[pc+1:pc+5]
            pc += 5
        aa += p[pc+1:pc+5]
        pc += 5
        pp = int(aa, 2)
        ss = str(pp)

    s += v
    return pc, pp, ss

print(parse(0)[1])
print(s)
print(((13 + 3 + 15) * (14 + 3 + 5) * (4 + 12 + 10)) + ((1398 == 3746) * 3130) + min([224560, 136, 12024489]) + 517270 + 2 + (213 * 115 * 186 * 225 * 54) + ((97 < 171) * 140) + (4162186587) + 6684131 + (149 * 60) + (213 * 10 * 7) + 10 + ((887685 < 23) * 3924) + (max([((max([(min([(max([(max([((min([((((max([(4087)])))))])))]))]))]))])))])) + 2047 + (1256 * ((9 + 10 + 12) > (14 + 11 + 15))) + (1657 * (232 < 6)) + max([7, 3818, 37218785, 46712960]) + max([51492, 54252, 13, 9637, 3673]) + (((7 + 6 + 13) > (13 + 4 + 13)) * 25) + ((11 * 9 * 8) + (2 * 2 * 12) + (8 * 6 * 13)) + (55844 * (49 > 313815)) + max([3923, 15, 925937357972]) + ((2068 < 2068) * 716758659) + 509679249895 + min([303, 200, 211471, 17, 1859699]) + min([32948, 13810293, 1060, 3]) + ((7201310 > 7201310) * 802492) + ((1008504 > 1614) * 63476) + (((15 + 5 + 9) == (8 + 12 + 7)) * 352360) + (((9 + 10 + 14) < (11 + 5 + 8)) * 3278) + max([20677, 103]) + (119 * (189 == 189)) + (25382 * (3729 > 334701)) + (68) + (135 * 171 * 32 * 251) + min([2381, 2645]) + (1715 + 227327288) + (4 + 17253 + 9) + (2485 * (11 < 151523)) + ((245459830 > 12341) * 1) + (39533 * (15033999 == 25441)) + max([22]) + min([12]) + 140679419 + (188 + 152 + 84716 + 213 + 32351) + (29 + 5 + 31224 + 8) + 647867 + (52864 * (48615 > 48615)) + 214996849 + (92 * (151 < 151)) + 696031 + (610123 * ((10 + 12 + 9) < (14 + 4 + 8))))