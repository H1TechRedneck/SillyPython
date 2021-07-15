# This programm demonstrates what luck is
# So
# Good luck pal

import random



print("You eaten a pie, but something was inside, Oh gosh, it's surprise...")
print("and your suprprise is...")

value = random.randint(1,5)

if value == 1:
    print(\
     """
       __,_____
     / __.==--"
    /#(-'
    `-'
     
     """)

elif value == 2:
    print(\
     """
      /| ________________
O|===|* >________________>
      \|
     
     """)

elif value == 3:
    print(\
     """   
     .-.
   __| |__
  [__   __]
     | |
     | |
     | |
     '-' 
        
     """)

elif value == 4:
    print(\
    """
       .:'
      __ :'__
   .'`__`-'__``.
  :__________.-'
  :_________:
   :_________`-;
    `.__.-.__.'

    """)

elif value == 5:
    print(\
    """    
`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
         (_,'


       """)

else:
    print ("Sorry, but you have nothing here, just enjoy your pie")

print ("Wow.... so.....well, IDK what do you need it for, but who am I to judging you")

input("\n\nPress the enter key to exit.")