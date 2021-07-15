""" 
Карочи, программа реально создает название наиболее подходящего для тебя  блюда, 
на основе двух твоих любимых блюд
"""
print("Hey partner, are you ready to see name of your new favorite food?")

yn=input("Y/N?\n")

if yn=="Y":
  print("You goddamn right, let's start then\n")
elif yn=="N":
  print("Nah man, but I give you a second chance. So let's do it anyway\n")
else:
  print("Try again")

food1=input("So, please call me name of your first favorite food\n")
print("\nAwesome, go forward")

food2=input("And now, tell me what's name of your second favorite food?\n")
print("\nOk dude, I'll check this information to provide you a best match that you ever seen")

super_food=food1+food2

print("\nAaaaaaaaaaaaaand we got a name, your best food is", super_food)

input("\nsPress Enter to go away")