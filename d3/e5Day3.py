# Exercise 5 - Love Calculator 💌

# Instructions
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

namesTogether =  name1 + name2

checkName = namesTogether.lower()
 

tScore = checkName.count('t') 
rScore = checkName.count('r')
uScore = checkName.count('u') 
eScore = checkName.count('e') 


lScore = checkName.count('l')
oScore = checkName.count('o')
vScore = checkName.count('v') 
eScore = checkName.count('e') 

true =  tScore + rScore + uScore + eScore
love = lScore  + oScore + vScore + eScore

trueLove = str(true) + str(love)

totalScore = int(trueLove)


if totalScore < 10 or totalScore > 90:
    print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore > 40 and totalScore < 50:
    print(f"Your score is {totalScore}, you are alright together.")
else:
    print(f"Your score is {totalScore}")