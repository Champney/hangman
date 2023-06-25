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
        print(f"The mistery word has {self.num_letters} characters")
        print(f"{self.word_guessed}")
        pass

    def ask_letter(self):
        while True:
            letter = input("Please enter a letter as your guess: ")
            if len(letter) != 1 or letter.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif letter in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_letter(letter)
                self.list_of_guesses.append(letter)
        pass

    def check_letter(self, letter) -> None:
        self.guess = letter.lower()
        if self.letter in word:
            print(f"Good guess! {self.letter} is in the word.")
            for i in range(len(word)):
                if word[i] == self.letter:
                    self.word_guessed[i] = self.letter
            self.num_letters -= 1
               
        else:
            print(f"Sorry, {self.letter} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
        pass

    


    
    

