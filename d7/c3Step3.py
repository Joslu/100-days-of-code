''' STEP 3 '''

import random 

word_list = ["pearl", "camel", "dinosaurs", "paper", "welcome"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f"Pfff the solution is {chosen_word}")

#Create blanks 
display = []

for _ in range(word_length):
    display += "_"

# TODO-1: 
# Use a while loop to let the user 
# guees again. The loop shoul only stop once 
# the user has guessed all the letter in the 
# chosen_word and 'display' has no more 
# blanks ("_"). Then you can tell the user 
# they've won.

 
endGame = False;

while not endGame:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    print(display)

    if not '_' in display:
        endGame = True
        print("You have won!")