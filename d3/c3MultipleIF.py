print("Welcome to the rollercoaster!")

height = int(input("What is your heigh in cm???: "))


bill = 0

if height > 120:
    print("You can ride the rollercoaster! 😃")
    age = int(input("What's ypur age???: "))

    if age >= 18:
        bill = 10
        print(f"Ticket ${bill} 💸")
    elif 12 < age < 18:
        bill = 8
        print(f"Ticket${bill}")
    else:
        bill = 5
        print(f"Ticket ${bill}")

    wantsPhoto =input("Do you want photos Y/N???: ")

    if wantsPhoto == 'Y':
        bill += 5

    print(f"Please, pay ${bill}")



else:
    print("Sorry you can't 😢")