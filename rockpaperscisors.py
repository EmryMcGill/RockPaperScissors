import random

#welcome user
print ("Welcome to")
print ("Rock | Paper | Scisars")
print ()
print ()

values = ["s","r","p"]

#input
userVal = input("Rock[R] Paper[P] Scisars[S]: ")

oppval = random.choice(values)

#testing

userVal.lower()

print ("Opponent choses " + oppval)

#opp rock
if oppval == "r" and userVal == "s":
    print ("You Lose")

if oppval == "r" and userVal == "p":
    print ("You Win!")

if oppval == "r" and userVal == "r":
    print ("It's a tie!")

#opp Scisars
if oppval == "s" and userVal == "r":
    print ("You Win!")

if oppval == "s" and userVal == "p":
    print ("You lose")

if oppval == "s" and userVal == "s":
    print ("It's a tie!")
