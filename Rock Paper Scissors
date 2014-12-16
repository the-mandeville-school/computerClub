# Create a game to guess Rock, Paper, Scissors.
#
# Rock(0) beats Scissors(2)
# Scissors(2) beats Paper(1)
# Paper beats Rock
# Paper draws with Paper
# Scissors draws Scissors
# Rock draws with Rock
#

import random
loop1=False

# Store all the possible predictions
rps = ["Rock","Paper","Scissors"]
human = -1

# Greeting, and explain the game
print("Hi, I'm the computer. We're playing Rock, Paper, Scissors.")

while human < 0 or human > 2:

    print("Take a guess from the list below: (1-3)")
    print("")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")

    # Get the human prediction
    #
    human = int(raw_input())-1
    if human < 0 or human > 2:
        print "Sorry, I don't recognise that request."

print("You have predicted, "+ rps[human])

# Get the computer prediction

computer = random.randint(0,2)

print("Computer has predicted, " + rps[computer])

# Compare human to computer
#

if human == 0 and computer == 2:
    print("Well done you win")

if human == 1 and computer == 0:
    print("Well done you win")



# Decide who wins
