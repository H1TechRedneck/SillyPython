#
#
#


import random


throw_up = 0
orel = 0
reshka = 0

while throw_up < 100:
    throw_up += 1
    
    coin_sides=random.randint(1,2)
    
    if coin_sides == 1:
        orel += 1
    
    elif coin_sides ==2:
        reshka += 1

print ("And orel is",orel, )

print ("\nAnd reshka is...", reshka,)    
    



