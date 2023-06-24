# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.
# Milestone 2 
## Task 1
### Define the list of possible words and assign them to a variable called word_list, print the output to the screen
This consisted of manually inputting a list of fruit and assigning the list to a variable called 'words'.
After that it was simply a matter of calling the print function and passing 'words' as an argument

## Task 2
### Choose a random word from the list
This consisted of importing the 'random' module and using the 'random.choice' method to select a random element from the list 'words'
After that, I assigned random.choice to a variable 'word' and called it inside the print argument in order to print the randomly selected word

## Task 3
### Ask the user for input
This was a matter of writing a single line of code that equated the user input function to the variable 'guess'

## Task 4
### Check that the input is a single character and alphabetical
In order to do this, I included a nested if-else statement. The outer if-else statement used the len() and alpha() methods to test whether the user input was both one character long and alphabetical.
The inner if-else statement checked whether the user input was in the randomly generated word

# Milestone 3

## Task 1
### Iteratively check if the input is a valid guess
To achieve this, I created a while loop and set the default condition to True, then I set the 'guess' variable as an input.
Then, all I needed to do was create an if statement to check whether the user input was both one character long and alphabetical, and add a break clause to trigger when the condition is met.
If the condition wasn't met, the else statement would print "Invalid letter. Please, enter a single alphabetical character."

## Task 2
### Check whether the guess is in the word
This was a matter of writing an if-else statement that checks whether the user input is present in the variable 'word'

## Task 3
### Create the functions to run the checks
All I needed to do here was encapsulate and tidy the code i had already written. I created a check_guess function which took one parameter, 'guess', and a function 'ask_for_input'.
The 'check_guess' function took the user input, converted it to lower case and checked whether or not it was in the variable 'word'.
The 'ask_for_input' function contained the preceding while loop followed buy the 'check_guess' function with 'guess' passed as the argument.

