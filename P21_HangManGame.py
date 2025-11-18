import random

words = ["Zameel" , "Naweed" , "Apple", "Orange" , "Elephant" , "Lion" , "Youtube"]

ran_choice = random.choice(words).upper()

display = ["_"]*len(ran_choice)


print("Welcome To The Hang-Man-Game")
print("You Need to Guess the Word ")
print(f"The lenth of the word is  {len(ran_choice)}")
print(" ".join(display))

attempts = 6
guessd_words = []

while "_" in display and attempts > 0:
    u_words = input("Please Enter a Word").strip().upper()

    if u_words in guessd_words:
        print("You alrady guessed the letter")
        continue

    guessd_words.append(u_words)

    if u_words in ran_choice:
        for i, letter in enumerate(ran_choice):
            if letter == u_words:
                display[i] = u_words

        print("Good Guess")


    else:
        attempts -= 1
        print(f"❌ Wrong guess! You lost a life. Lives left: {attempts}")

    print("Word: ", " ".join(display))
    print("Guessed letters:", ", ".join(guessd_words))
    print()



if "_" not in display:
    print("🎉 Congratulations! You guessed the word:", ran_choice)
else:
    print("💀 Game Over! The word was:", ran_choice)


