import random

word_list = ["apple"]


class Hangman:

    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = list("_"* len(self.word))
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []


      
    def check_guess(self,guess):
        #checks user input aka guess to see if exists in word.
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            """ For loop below will iterate through length of word and check if each position/index is equal 
            to guessed letter, if equal to guessed letter, will edit the word_guessed ["_","_" ... ] 
            at the appropriate position/ index, printing word_guessed will display guessed letter at 
            appropriate position. """

            for position in range(len(self.word)):
                letter = self.word[position]
                if letter == guess:
                    self.word_guessed[position] = letter
                    print(self.word_guessed)
                self.num_letters -= 1
        else:
            self.num_lives -= 1
            letter = guess 
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


      
    def ask_for_input(self):
        #checks to see if input is valid. single letter. isalpha only.
        #feeds check_guess method.
        while True:
            guess = str(input("Guess a single letter: "))
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")  
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.list_of_guesses.append(guess)
                #print(self.list_of_guesses)
                self.check_guess(guess)
                
                

   


game = Hangman(word_list)
game.ask_for_input()
