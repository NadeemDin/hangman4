import random

#word list of guess words
word_list = ["apple", "banana", "pear", "grape", "strawberry"]
print(word_list)
word = random.choice(word_list)
print(word)

#user input to guess letters
guess = input(str(f"Guess a single letter?: ")).lower()

if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz":
    print(f"Good guess!")
else:
    print("Oops! That is not a valid input")

