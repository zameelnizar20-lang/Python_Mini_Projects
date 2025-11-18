import random

type_choice = ("r" , "p" , "s")



while True:
    ran =  random.choice(type_choice)
    user_choice = input("Please select your choice ('r/p/s') :")

    if user_choice == ran :
        print("The game is tie")
        print(f"Your choice is : {user_choice}")
        print(f"Computer Choice is : {ran}")

    elif \
        (user_choice == "r" and ran == "s") or \
        (user_choice == "s" and ran == "p") or \
        (user_choice == "p" and ran == "r"):
        print("You Win the game !!")
        print(f"Your choice is : {user_choice}")
        print(f"Computer Choice is : {ran}")

    else:
        print("Computer Wins the game")
        print(f"Your choice is : {user_choice}")
        print(f"Computer Choice is : {ran}")