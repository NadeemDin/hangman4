import random

#word list of guess words
word_list = ["apple", "banana", "pear", "grape", "strawberry"]


word = random.choice(word_list)
print(word)

#user input to guess letters


guess = input(str(f"Guess a single letter?: ")).lower()

if len(guess) == 1 and guess.isalpha():
    print(f"Good guess!")
else:
    print("Oops! That is not a valid input")

