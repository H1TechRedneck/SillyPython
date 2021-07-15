#This is programm that will be assist you calculate a real price of a new car with all additional required payments that you'll pay when you buy a new car.

print("Hey friend,I heard you would like to buy a new car, It's awesome, but do you know what's real car price is?")
print("\nI can help you understand how much cost your new car with all extra charge that you gonna pay")
#payments based on car price: Tax= 13%, registration tax= 9% 
car_price=float(input("\nSo, tell me, what's raw price of your car:\n"))
tax=car_price*0.13
Reg_tax=car_price*0.09

delivery=float(input("\nHow much does delivery cost from store to your house?\n"))
agent_tax=float(input("\nHow much agent usually get?\n"))

real_price=car_price+delivery+agent_tax+tax+Reg_tax
print("\nOk, then let me calculate а real price")
input("\nPress Enter to know how much money i need")

print("\nSo your real car price is", real_price)

details=input("\nIf you would like to know details what the total cost consists of send \"Yes\"\n")

if details=="Yes":
  print("\n1)So let's start from scratch, car that you want to buy price is",car_price)
  print("\n2)As you definitely know, when you buy a new car, you should pay some tax, at this case tax is",tax)
  print("\n3)And of couse you should pay registration tax, thad based on initial price of your car as a usual tax, registration tax is",Reg_tax)
  print("\n4)When you buy a new car, employe that will formalize this purchase also should get a some money, this usually calls agent tax or something, and usually agent tax fixed at specific place, at this case agent tax is", agent_tax)
  print("\n5)And finally car cannot go to your house by itself, someone should deliver this to you, delivery also costs some money as you supposed to know, delivery from store to your house will be price is", delivery)
  print("\nIf you summary all this values you'll get a real price (", real_price, ") of car that you want to buy")

elif details=="No":
  print("\nOk, that's fine I see you dont care, bue then and I wish you have a good shopping")
else:
  print("\nI don't get it sir, I guess you're drunk or something and you shouldn't drive and buy a car now, see ya")
  
input("\nPress Enter to end of this session")