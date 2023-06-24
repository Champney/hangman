word_list = ['mango', 'watermelon', 'kiwi', 'raspberry', 'lime']
print(word_list)

import random
choice = random.choice(word_list)
print(choice)
guess = input()

word_expressed_as_list = list(choice)
if len(guess) == 1 and guess.isalpha() == True:
    if guess in word_list:
        print("Good guess!")
    elif guess not in word_list:
        print("Try again!")
else:
    print("Oops! that is not a valid input")
