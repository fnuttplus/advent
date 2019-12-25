deck = list(range(10007))

#print(deck)

from sys import stdin
for line in stdin.read().splitlines():
    l = line.split(" ")
    if len(l) == 2:
        i = int(l[-1])
        #print("cut", i)
        deck = deck[i:] + deck[:i]
    else:
        if l[1] == "with":
            i = int(l[-1])
            #print("deal", i)
            deck0 = deck[:]
            for x in range(len(deck)):
                deck[(x*i)%len(deck)] = deck0[x]
        else:
            #print("deal stack")
            deck.reverse()
#print(deck)
print(deck.index(2019))