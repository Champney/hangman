word_list = ['mango', 'watermelon', 'kiwi', 'raspberry', 'lime']
print(word_list)

import random
choice = random.choice(word_list)
word = choice
print(word)
print(word)
print(word)
print(word)
guess = input()

word_expressed_as_list = list(word)
if len(guess) == 1 and guess.isalpha() == True:
    if guess in word_list:
        print("Good guess!")
    elif guess not in word_list:
        print("Try again!")
else:
    print("Oops! that is not a valid input")
