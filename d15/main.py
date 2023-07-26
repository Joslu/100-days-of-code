import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "milk": 200,
    "water": 300,
    "coffee": 100,
}

userTextPrompt = """What would you like? (Select with number):
1. Espresso 
2. Latte
3. Cappuccino
-----------------------------------------

"""


def generate_report():

    print(f"""
    Milk: {resources["milk"]} ml
    Water: {resources['water']} ml
    Coffee: {resources['coffee']} ml
    """)


def check_resources():
    pass


def process_coins():
    pass


def check_transaction():
    pass


def make_coffe():
    pass


def main():
    is_on = True

    while is_on:

        user_choice = input(userTextPrompt).lower()

        if user_choice == 'report':
            generate_report()
            time.sleep(4)
        elif user_choice == 'off':
            is_on = False

        elif user_choice in MENU:
            print(user_choice)
            time.sleep(4)
        else:
            print('Invalid command, try with another one')
            time.sleep(4)


if __name__ == "__main__":
    main()
