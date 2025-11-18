#Lets create a Dice Roller Game
import random

while True:
    user = input("Do you whant to Dise the roll ('y/n') :")
    if user == "y":
        roll = random.randint(1,6)
        print(roll)

    elif user == "n":
        break

    else: 
        print("Invalid Output")




    