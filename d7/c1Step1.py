'''
    ********* STEP 1 ***********
'''

from random import randint, random


word_list = ["ardvark", "camel", "bee", 'dog', 'increase']

## TODO-1
# Randomly choose a word from the word_list and
# assign it to a variable called chosen_word.


##chosen_word = random.choice(word_list)

chosen_word = word_list[randint(0, len(word_list) - 1)]
print(chosen_word)

## TODO-2
# Ask the user to guess a letter and assign
# their answer to a variable called guess.
# Make guess lowercase.

userGuess = input('Guess a letter from the word: ').lower()


##TODO-2
# loop through each position in the chosen_word;
# If the lettet at that position matches 'guess' then
# reveal that letter in the display at that position.
# e.g If the user guesssed "p" and the chosen word was
# 'apple', then display should be ["-", "p", "p", "-", "-"].

## TODO-3
# Check if the letter the user guessed (guess)
# ir one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == userGuess:
        print(letter)
    else:
        print('_')
 
'''
    ********* STEP 2 ***********
'''

# TODO-1 
# Create an empty list called display,
# For each letter in the chosen_word, add a "_" to 'display'
# So if the chosen_word was 'apple', display should be
# ["_", "_", "_", "_", "_"] with 5 "_" representing each
# letter to guess.