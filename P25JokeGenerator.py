import random 

JOKES = [    "I told my computer I needed a break, and it said: 'No problem — I'll go to sleep.'",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why don't programmers like nature? Too many bugs.",
    "Why do Java developers wear glasses? Because they don't see sharp."]


def select_jokes(joke_list):
    if not joke_list:
        raise ValueError("There is no jokes in the list")
    
    selected = random.choice(joke_list)
    return selected


def main():
    called = select_jokes(JOKES)
    print(called)


main()