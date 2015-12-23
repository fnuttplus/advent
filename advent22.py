from itertools import product

"""
Player:
HP: 50
Mana: 500

Boss:
Hit Points: 58
Damage: 9

Magic Missile manas 53 mana.
	It instantly does 4 damage.
Drain manas 73 mana.
	It instantly does 2 damage and heals you for 2 hit points.
Shield manas 113 mana.
	It starts an effect that lasts for 6 turns.
	While it is active, your armor is increased by 7.
Poison manas 173 mana.
	It starts an effect that lasts for 6 turns.
	At the start of each turn while it is active, it deals the boss 3 damage.
Recharge manas 229 mana.
	It starts an effect that lasts for 5 turns.
	At the start of each turn while it is active, it gives you 101 new mana.
"""

def spentmana(actions):
	mana = 0
	for a in actions:
		if a == "Missile": mana += 53
		elif a == "Drain": mana += 73
		elif a == "Shield": mana += 113
		elif a == "Poison": mana += 173
		elif a == "Recharge": mana += 229
	return mana

def playerwins(actions, verbose=False):
	playerHP,mana = 50, 500
	bossHP, bossD = 58, 9
	turn = 1
	shieldT, poisonT, rechargeT = 0,0,0
	while True:
		if verbose: print("\n--- Turn", turn, "---")

		if shieldT > 0:
			shieldT -= 1
			if verbose: print("Shield' timer is now", shieldT)
		if poisonT > 0:
			bossHP -= 3
			poisonT -= 1
			if verbose: print("Poison deals 3 damage; its timer is now", poisonT)
		if rechargeT > 0:
			mana += 101
			rechargeT -= 1
			if verbose: print("Recharge provides 101 mana; its timer is now", rechargeT)

		if turn % 2 == 1 and turn < len(actions)*2:
			if verbose: print("-- Player turn --")
#			if verbose: print("This is hard mode! Player takes one damage!")
#			playerHP-=1
			if verbose: print("Player casts ", end="")
			if actions[turn//2] == "Missile":
				mana -= 53
				bossHP -= 4
				if verbose: print("Magic Missile, dealing 4 damage!")
			elif actions[turn//2] == "Drain":
				mana -= 73
				bossHP -= 2
				playerHP += 2
				if verbose: print("Drain, dealing 2 damage, and healing 2 hit points!")
			elif actions[turn//2] == "Shield":
				if shieldT > 0: return False
				mana -= 113
				shieldT = 6
				if verbose: print("Shield, increasing armor by 7!")
			elif actions[turn//2] == "Poison":
				if poisonT > 0: return False
				mana -= 173
				poisonT = 6
				if verbose: print("Poison!")
			elif actions[turn//2] == "Recharge":
				if rechargeT > 0: return False
				mana -= 229
				rechargeT = 5
				if verbose: print("Recharge!")
			if mana <= 0: return False
		else:
			if verbose: print("-- Boss turn --")
			playerHP -= (bossD-7 if shieldT else bossD)
			if verbose: print("Boss attacks for", "9 - 7 = 1" if shieldT else "9", "damage!")
		if verbose: print("- Player has", playerHP, "hit points,", 7 if shieldT else 0, "armor,", mana, "mana.")
		if verbose: print("- Boss has", bossHP, "hit points.")
		if bossHP <= 0:
			if verbose: print("\nBoss is slain! Player spent", spentmana(actions), "mana.")
			return True
		if playerHP <= 0:
			return False
		turn += 1

#magicks = ["Missile", "Drain", "Shield", "Poison", "Recharge"]

#minmana = 2000
##5^9 = 1953125
#for p in product(magicks, repeat=9):
#	if playerwins(p):
#		mana = spentmana(p)
#		if mana < minmana:
#			print(p,mana)
#			minmana = mana

#playerwins(["Poison","Recharge","Shield","Poison","Recharge","Shield","Poison","Missile","Missile"], True)
playerwins(('Poison', 'Missile', 'Recharge', 'Poison', 'Shield', 'Recharge', 'Poison', 'Drain', 'Missile'), True)
