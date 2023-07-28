from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

is_on = True

while is_on:

    options = my_menu.get_items()
    user_choice = input(f'What would you like? {options}')

    if user_choice == 'off':
        is_on = False

    elif user_choice == 'report':
        print(my_machine.report())
        print(my_coffee_maker.report())

    else:
        drink = my_menu.find_drink(user_choice)

        if my_coffee_maker.is_resource_sufficient(drink) and my_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)
