
word = input("Please Type a word : ")

if word[::-1] == word:
    print("This is a palindrome")

else:
    print(word)


print(word[::-1])