word_list = ['mango', 'watermelon', 'kiwi', 'raspberry', 'lime']
print(word_list)
import random
word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = word
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = ["_"] * len(word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        pass
    
    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter as your guess: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def check_guess(self, guess):
        self.guess = guess.lower()
        if self.guess in word:
            print(f"Good guess! {self.guess} is in the word.")
            for i in range(len(word)):
                if word[i] == self.guess:
                    self.word_guessed[i] = self.guess
            self.num_letters -= 1
                
        else:
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
 

    


    
    

