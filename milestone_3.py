import random

word_list = ["apple", "banana", "pear", "grape", "strawberry"]
word = random.choice(word_list)
print(word)

def ask_for_input():
    guess = str(input("Guess a single letter: ")).lower()
    check_guess(guess)


def check_guess(guess):
    while True:

        if guess.isalpha() and len(guess) == 1:
            if guess in word:
                print(f"Good guess! {guess} is in the word.")
            else:
                print(f"Sorry, {guess} is not in the word.")
            break
        else:
            print(f"Invalid letter. Please, enter a single alphabetical character.")
            guess = ask_for_input()

ask_for_input()




