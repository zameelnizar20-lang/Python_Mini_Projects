import random

computer_number = random.randint(1,10)
attempt = 0

while True:
    user_input = int(input('Guess a number : '))
    print(f"Computer Guess is : {computer_number}")
    print(f"Your Guess is : {user_input}")

    if computer_number == user_input:
        attempt += 1
        print(f"You have taken {attempt} attempts to guess the correct answer")
        print("You Won ! Your Guess is Corrct")
        break

    if computer_number > user_input:
        attempt += 1
        print(f"You have taken {attempt}")
        print("Your number is to Low ")

    elif computer_number < user_input:
        attempt += 1
        print(f"You have taken {attempt}")
        print("Your number is to High ")
    
    else:
        print("Somthing Went Wrong")