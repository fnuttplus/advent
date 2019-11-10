import re

immune_system = [
    {"units": 2334, "initiative": 4, "hit_points": 8900, "damage": [31, "fire"], "weak": [], "immune": []},
    {"units": 411, "initiative": 1, "hit_points": 8067, "damage": [195, "radiation"], "weak": [], "immune": []},
    {"units": 449, "initiative": 3, "hit_points": 9820, "damage": [193, "bludgeoning"], "weak": ["fire"], "immune": []},
    {"units": 452, "initiative": 10, "hit_points": 4418, "damage": [89, "bludgeoning"], "weak": ["fire"], "immune": ["bludgeoning"]},
    {"units": 858, "initiative": 18, "hit_points": 5016, "damage": [58, "bludgeoning"], "weak": ["bludgeoning", "fire"], "immune": ["slashing"]},
    {"units": 3049, "initiative": 12, "hit_points": 9940, "damage": [29, "cold"], "weak": [], "immune": []},
    {"units": 610, "initiative": 7, "hit_points": 7021, "damage": [114, "fire"], "weak": ["bludgeoning","radiation"], "immune": []},
    {"units": 4033, "initiative": 5, "hit_points": 8807, "damage": [21, "cold"], "weak": ["radiation"], "immune": []},
    {"units": 1209, "initiative": 20, "hit_points": 7468, "damage": [50, "radiation"], "weak": ["fire"], "immune": ["cold"]},
    {"units": 3228, "initiative": 14, "hit_points": 7550, "damage": [21, "slashing"], "weak": ["cold"], "immune": ["bludgeoning","radiation"]},
]

infection = [
    {"units": 1230, "hit_points": 36915, "damage": [58, "bludgeoning"], "initiative": 16, "weak": ["cold", "slashing"], "immune": []},
    {"units": 629, "hit_points": 23164, "damage": [72, "slashing"], "initiative": 11, "weak": [], "immune": []},
    {"units": 266, "hit_points": 16518, "damage": [113, "fire"], "initiative": 2, "weak": [], "immune": []},
    {"units": 45, "hit_points": 17769, "damage": [774, "fire"], "initiative": 19, "weak": [], "immune": ["radiation", "slashing", "bludgeoning", "fire"]},
    {"units": 93, "hit_points": 32105, "damage": [535, "fire"], "initiative": 8, "weak": ["fire"], "immune": []},
    {"units": 957, "hit_points": 19599, "damage": [32, "cold"], "initiative": 15, "weak": [], "immune": ["cold"]},
    {"units": 347, "hit_points": 29661, "damage": [170, "bludgeoning"], "initiative": 17, "weak": [], "immune": []},
    {"units": 418, "hit_points": 17587, "damage": [73, "bludgeoning"], "initiative": 6, "weak": ["cold", "radiation"], "immune": ["fire", "slashing"]},
    {"units": 2656, "hit_points": 49851, "damage": [32, "radiation"], "initiative": 9, "weak": [], "immune": []},
    {"units": 5365, "hit_points": 35984, "damage": [13, "radiation"], "initiative": 13, "weak": [], "immune": []}
]

"""
immune_system = [
    {"units": 17, "initiative": 2, "hit_points": 5390, "damage": [4507, "fire"], "weak": ["radiation", "bludgeoning"], "immune": []},
    {"units": 989, "initiative": 3, "hit_points": 1274, "damage": [25, "slashing"], "weak": ["bludgeoning", "slashing"], "immune": ["fire"]},
]

infection = [
    {"units": 801, "hit_points": 4706, "damage": [116, "bludgeoning"], "initiative": 1, "weak": ["radiation"], "immune": []},
    {"units": 4485, "hit_points": 2961, "damage": [12, "slashing"], "initiative": 4, "weak": ["fire", "cold"], "immune": ["radiation"]},
]

def weak(s):
    s = re.search("weak to ([a-z,\s]*)", s)
    if s: return s.group(1).split(", ")
    return []

def immune(s):
    s = re.search("immune to ([a-z,\s]*)", s)
    if s: return s.group(1).split(", ")
    return []

def group(s):
    return {"units": int(s.group(1)), "hit_points": int(s.group(2)), "weak": weak(s.group(3)), "immune": immune(s.group(3)), "damage": [int(s.group(4)), s.group(5)], "initiative": int(s.group(6))}
immune_system = []
infection = []
input()
for _ in range(10):
    s = re.search("(\d*) units each with (\d*) hit points (.*)with an attack that does (\d*) (.*) damage at initiative (\d*)", input())
    immune_system.append(group(s))
input()
input()
for _ in range(10):
    s = re.search("(\d*) units each with (\d*) hit points (.*)with an attack that does (\d*) (.*) damage at initiative (\d*)", input())
    infection.append(group(s))

for group in immune_system: print("{} units each with {} hit points (weak to {}; immune to {}) with an attack that does {} {} damage at initiative {}".format(group["units"], group["hit_points"], ", ".join(group["weak"]), ", ".join(group["immune"]), group["damage"][0], group["damage"][1], group["initiative"]))
for group in infection: print("{} units each with {} hit points (weak to {}; immune to {}) with an attack that does {} {} damage at initiative {}".format(group["units"], group["hit_points"], ", ".join(group["weak"]), ", ".join(group["immune"]), group["damage"][0], group["damage"][1], group["initiative"]))
"""

def selection_order(l):
    return sorted(enumerate(l), key=lambda x: (x[1]["units"] * x[1]["damage"][0], x[1]["initiative"]), reverse=True)

def damage_multiplier(x, t):
    if t in x["immune"]: return 0
    if t in x["weak"]: return 2
    return 1

def target_order(l, t):
    return sorted(enumerate(l), key=lambda x: (damage_multiplier(x[1], t), x[1]["units"] * x[1]["damage"][0], x[1]["initiative"]), reverse=True)

def target_selection(a, d, b):
    l = []
    for group in selection_order(a):
        if group[1]["units"] <= 0: continue
        for g2 in target_order(d, group[1]["damage"][1]):
            if damage_multiplier(g2[1], group[1]["damage"][1]) == 0: break
            if g2[1]["units"] <= 0: continue
            if not g2[0] in [x[2] for x in l]:
                l.append((group[1]["initiative"], group[0], g2[0], b))
                break
    return l

for i in range(len(immune_system)): immune_system[i]["damage"][0] += 29

def units_killed(b, c):
    if b["units"] <= 0: return 0
    return min(c["units"], (b["units"] * b["damage"][0] * damage_multiplier(c, b["damage"][1])) // c["hit_points"])

while sum([a["units"] for a in infection]) > 0 and sum([a["units"] for a in immune_system]) > 0:
    ts = sorted(target_selection(infection, immune_system, "a") + target_selection(immune_system, infection, "b"), reverse=True)

    for a in ts:
        if a[3] == "a":
            immune_system[a[2]]["units"]-=units_killed(infection[a[1]], immune_system[a[2]])
        else:
            infection[a[2]]["units"]-=units_killed(immune_system[a[1]], infection[a[2]])

#todo: find endless loop when two immune groups are left, by counting total number of units killed in a round?
print(sum([a["units"] for a in infection]), sum([a["units"] for a in immune_system]))