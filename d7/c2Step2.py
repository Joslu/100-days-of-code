''' STEP 2'''

import random 
word_list = ["pearl", "camel", "dinosaurs", "paper", "welcome"]
chosen_word = random.choice(word_list)

print(f"Pfff the solution is {chosen_word}")

userGuess = input("Guess a letter from the word: ")

##TODO-1
# Create an empty list called display,
# For each letter in the chosen_word, add a "_" to 'display'
# So if the chosen_word was 'apple', display should be
# ["_", "_", "_", "_", "_"] with 5 "_" representing each
# letter to guess.

display = []

##TODO-2
# loop through each position in the chosen_word;
# If the lettet at that position matches 'guess' then
# reveal that letter in the display at that position.
# e.g If the user guesssed "p" and the chosen word was
# 'apple', then display should be ["-", "p", "p", "-", "-"].

for character in range(0, len(chosen_word)):
    if chosen_word[character] == userGuess:
        display.append(userGuess)
    else:
        display.append("_")

print(display)

 
 
