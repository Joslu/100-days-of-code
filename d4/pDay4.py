# Rock Paper Scissors
# Instructions
# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.

# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.


import random


# 0 rock, 1 paper, 2 scissors

# 0 < 1
# 0 > 2

# 1 < 2






rock =  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


gameImages = [rock, paper, scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

print(gameImages[userChoice])

computerChoice = random.randint(0, 2)

print("Computer chose: ")
print(gameImages[computerChoice])


if userChoice >= 3 or userChoice < 0:
    print('Invalid choice from the user, you lose!')
elif userChoice ==  computerChoice:
    print('Same, play again!')
elif computerChoice == 0 and userChoice == 2:
    print('You lose!')
elif userChoice == 0 and computerChoice == 2:
    print('You win')
elif computerChoice > userChoice:
    print("You lose")
elif userChoice > computerChoice:
    print("You win!")