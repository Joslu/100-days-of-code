print("Welcome to the rollercoaster!")

height = int(input("What is your heigh in cm???: "))


if height > 120:
    print("You can ride the rollercoaster! 😃")
    age = int(input("What's ypur age???: "))

    if age >= 18:
        print("Please, pay $10 💸")
    elif 12 < age < 18:
        print("Please, pay $8")
    else:
        print("Please, pay $5")

else:
    print("Sorry you can't 😢")