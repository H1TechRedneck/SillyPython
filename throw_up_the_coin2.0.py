#
#
#
#

import random


print ("Hey, here you can try your luck with a coin, you will throw up your coin 100 times and bet on particular side of coin, if your side will be able to score more than other, you'll...nothing")




answer=""
while answer != "yes":
    answer=input ("Do you wanna throw up the coin?\n")
    if answer == "yes":
        print("Ok, then, let's get it champ\n")    
    else:
        print("Ok, then bye")

input ("Press Enter to continue")
    

which_side=input("Choose your side of coin\n")

if which_side == "orel":
    print ("\nOrel, Good choice")
elif which_side == "reshka":
    print("\nReshka, not as good as orel, but ok")
else:
    print("Ah, whatever, you'll get nothing as a prise anyway")

input("Press Enter to throw up your coin 100 times")


throw_up = 0
orel = 0
reshka = 0

while throw_up !=100:
    throw_up += 1
    coin_side = random.randint(1,2)
    if coin_side == 1:
        orel += 1
    elif coin_side == 2:
        reshka += 1

input("Press Enter to show your results")

print ("Congrats partner, you just throw up the coin 100 times and got orel- ",orel, "and reshka- ",reshka)

