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
    "water": 300,
    "milk": 100,
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
    Money: $ {profit}
    """)


def check_resources(coffe_ingredients):

    for ingredient in coffe_ingredients:
        if coffe_ingredients[ingredient] > resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}')
            return False
        return True


def process_coins():
    """Ask for money to the user"""
    print("Please insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, coffee_cost):
    """Return True when payment is accepted, or False when payment is rejected"""

    if money_received > coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f'Here is ${change} in change')
        global profit
        profit += coffee_cost
        return True
    else:
        print('Money not enough. Money refunded!')
        return False


def make_coffe(coffee_name, order_ingredients):
    """Make coffee, deduct the required ingredients"""

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f'''Here is your {coffee_name}!  ☕
    Enjoy! .
    ''')


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
            coffe = MENU[user_choice]

            print(user_choice)
            if check_resources(coffe['ingredients']):
                payment = process_coins()
                if is_transaction_successful(payment, coffe['cost']):
                    make_coffe(user_choice, coffe['ingredients'])


        else:
            print('Invalid command, try with another one')
            time.sleep(4)


if __name__ == "__main__":
    main()
