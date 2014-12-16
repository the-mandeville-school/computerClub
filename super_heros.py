# Author: Mr Williams
# Creation Date: 13/12/2014
#
# Program to create and maintain a set of Top Trump style cards
#


# Uses 'deque' objects to handle first-in last out type queues
from collections import deque
# Uses randomisation controls
from random import shuffle

attVal = 1
attDesc = 0
gameDeck = []

# Define constants for our cards
cNam = "Name"
cInt = "Intelligence"
cStr = "Strength"
cSpd = "Speed"
cDur = "Durability"
cEPr = "Energy Projection"
cFis = "Fighting Skills"

cAtt = [cNam, cInt, cStr, cSpd, cDur, cEPr, cFis]

# create our "table of cards" for player 1 and player 2

p1Cards =  ()
p2Cards = deque()
pileCards = deque()

# Create the fixed deck of all available cards for the game
deck = [
    ['Captain America', 3, 3, 2, 3, 1, 6],
    ['Iron Man', 6, 6, 5, 6, 6, 4],
    ['Loki Laufeyson', 5, 4, 7, 6, 6, 3],
    ['Thanos', 6, 7, 7, 6, 6, 4],
    ['The Hulk', 2, 7, 3, 7, 5, 4],
    ['Spiderman', 4, 4, 3, 3, 1, 4],
    ['Nick Fury', 3, 2, 2, 2, 1, 6]
    ]

# Create a sequence representing all cards in game

for i in range(len(deck)):
    gameDeck.append(i)

# Shuffle the cards into a random order
shuffle(gameDeck)
#print gameDeck

# Deal out ALL cards to both players
dealPlayer = 1
for heroID in gameDeck:
    if dealPlayer == 1:
        p1Cards.appendleft(heroID)
        dealPlayer = 2
    else:
        p2Cards.appendleft(heroID)
        dealPlayer = 1

# Main block
# Typical Game round, starts with player 1

while len(p1Cards) > 0 and len(p2Cards) > 0:
    p1HeroID = p1Cards.pop()
    p2HeroID = p2Cards.pop()
    p1Hero = deck[p1HeroID]
    p2Hero = deck[p2HeroID]
# Get length of Hero name to pad out the Attributes right justified
    hero1NameLen = len(p1Hero[0])
    hero2NameLen = len(p2Hero[0])

# List out all attributes, numbered 1 to 6 to enable selection to test against CPU
    print "Player one: {0:>{padName}}".format(p1Hero[0], padName=hero1NameLen + 12)
    print "=" * (hero1NameLen + 24)
    for attNum in range(1, 6 + 1):
        print "[{0}] {1}: {2:>{padLen}}".format(attNum, cAtt[attNum], p1Hero[attNum], padLen=hero1NameLen + 18 - len(cAtt[attNum]))

    print "=" * (hero1NameLen + 24)
    attChoice = -1
    while (attChoice < 0 or attChoice > 6):
        attChoice = int(raw_input("Choose Attribute number to compare [1-6] [0] to quit : "))

    print ""
    print "Player one: {0:>{padName1}}     Player two: {1:>{padName2}}".format(p1Hero[0], p2Hero[0], padName1=hero1NameLen + 12, padName2=hero2NameLen + 12)
    print "=" * (hero1NameLen + 24), "   ", "=" * (hero2NameLen + 24)
    for attNum in range(1, 6 + 1):
        if attNum == attChoice:
            print "v" * (hero1NameLen + 24), "   ", "v" * (hero2NameLen + 24)
        print "{0}: {1:>{padLen1}}     {2}: {3:>{padLen2}}".format(cAtt[attNum], p1Hero[attNum], cAtt[attNum], p2Hero[attNum],
            padLen1=hero1NameLen + 22 - len(cAtt[attNum]), padLen2=hero2NameLen + 22 - len(cAtt[attNum]))
        if attNum == attChoice:
            print "^" * (hero1NameLen + 24), "   ", "^" * (hero2NameLen + 24)

# Determine who wins and who loses
    if p1Hero[attChoice] > p2Hero[attChoice]:
        print "=" * len(p1Hero[0] + " beats " + p2Hero[0])
        print "{0} beats {1}".format(p1Hero[0], p2Hero[0])
        print "=" * len(p1Hero[0] + " beats " + p2Hero[0])
        p1Cards.appendleft(p1HeroID)
        p1Cards.appendleft(p2HeroID)
#Collect on table Pile of cards if required'
        while len(pileCards) > 0:
            p1Cards.appendleft(pileCards.pop())
    elif p1Hero[attChoice] < p2Hero[attChoice]:
        print "=" * len(p1Hero[0] + " defeated by " + p2Hero[0])
        print "{0} defeated by {1}".format(p1Hero[0], p2Hero[0])
        print "=" * len(p1Hero[0] + " defeated by " + p2Hero[0])
        p2Cards.appendleft(p2HeroID)
        p2Cards.appendleft(p1HeroID)
#Collect on table Pile of cards if required'
        while len(pileCards) > 0:
            p2Cards.appendleft(pileCards.pop())
    else:
        print "Draw, add cards to unclaimed pile"
        pileCards.append(p1HeroID)
        pileCards.append(p2HeroID)
        for pileID in pileCards:
            pHero = deck[pileID]
            print "{0}".format(pHero[0])
# List in-hand card quantity after round
    print "Cards in hand, player one: {0} v player two {1}".format(len(p1Cards), len(p2Cards))
print "Game Over"

    # List entire hands of both players, in order of play
print "Player 1:"
while len(p1Cards) > 0:
    pHero = deck[p1Cards.pop()]

print "Player 2:"
while len(p2Cards) > 0:
    pHero = deck[p2Cards.pop()]
    print "{0}: {1}".format(cNam[attDesc], pHero[cNam[1]])
