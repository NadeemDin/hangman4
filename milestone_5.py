import random

# TO TEST, LIMIT TO ONE WORD
word_list = ["apple","banana","mango","pineapple","cherry","avocado"]

#MESSAGES USING GENERATED ASCII ART

game_over_message = """
   _________    __  _________   ____ _    ____________     
  / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \    
 / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ /    
/ /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/     
\____/_/__|_/_/ _/_/_____/ __\____/_|___/_____/_/ |_|      
\ \/ / __ \/ / / /  / /   / __ \/ ___// ____/ /            
 \  / / / / / / /  / /   / / / /\__ \/ __/ / /             
 / / /_/ / /_/ /  / /___/ /_/ /___/ / /___/_/              
/_/\____/\____/  /_____/\____//____/_____(_)               
                                                           
 """

winning_message = """
   __________  _   ____________  ___  ___________ __
  / ____/ __ \/ | / / ____/ __ \/   |/_  __/ ___// /
 / /   / / / /  |/ / / __/ /_/ / /| | / /  \__ \/ / 
/ /___/ /_/ / /|  / /_/ / _, _/ ___ |/ /  ___/ /_/  
\____/\____/_/ |_/\____/_/ |_/_/__|_/_/__/____(_)   
\ \/ / __ \/ / / /  | |     / /  _/ | / / /         
 \  / / / / / / /   | | /| / // //  |/ / /          
 / / /_/ / /_/ /    | |/ |/ // // /|  /_/           
/_/\____/\____/     |__/|__/___/_/ |_(_)            
                                                    
"""


class Hangman:

    def __init__(self,word_list,num_lives):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = list("_"* len(self.word))
        self.num_letters = int(len(set(self.word))+1)
        self.num_lives = num_lives
        self.list_of_guesses = []

   

    def draw_hangman(self):
        lives = self.num_lives
        hangman_art = [
            '''
               -----
               |   |
                   |
                   |
                   |
                   |
            ----------
            ''',
            '''
               -----
               |   |
               O   |
                   |
                   |
                   |
            ----------
            ''',
            '''
               -----
               |   |
               O   |
               |   |
                   |
                   |
            ----------
            ''',
            '''
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            ----------
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            ----------
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            ----------
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            ----------
            '''
        ]
        print(hangman_art[6 - lives])


      
    def check_guess(self,guess):
        # checks user input aka guess to see if exists in word.

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
                    #print(self.word_guessed)
                    self.num_letters -= 1
                    #print(self.num_letters)


        else:
            self.num_lives -= 1
            letter = guess 
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            self.draw_hangman()
            
        print(self.word_guessed)   
                


      
    def ask_for_input(self):
        # checks to see if input is valid. single letter. isalpha only.
        # feeds check_guess method.

        while self.num_lives > 0 and self.num_letters > 0:
            guess = str(input("\nGuess a single letter: "))
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")  
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.list_of_guesses.append(guess)
                # print(self.list_of_guesses)
                self.check_guess(guess)
                
                

   
def play_game(word_list):
    # defines lives, creates instance of class game, defines rules for lives/playthrough.
    num_lives = 5 # min lives = 1 , max lives = 6
    game = Hangman(word_list, num_lives)
    
    while True:
        game.ask_for_input()
        if game.num_lives == 0:
            print(game_over_message)
            print(f"The word was {game.word}\n")
            break
        elif game.num_letters == 0:
            print(winning_message)
            break
        
   

   
        

play_game(word_list)