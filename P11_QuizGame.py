quiz = [
    ["What is the capital of France?", "Paris"],
    ["What is 5 × 6?", "30"],
    ["What color is the sky on a clear day?", "blue"]
]

score = 0

for item in quiz:
    questions = item[0]
    answers = item[1]

    user_input = input(questions + ":").strip()

    if user_input.lower() == str(answers).lower():
        print("Correct")
        score += 1
        print(f"Your Current score is {score}")

    else :
        print("Something Fishing")