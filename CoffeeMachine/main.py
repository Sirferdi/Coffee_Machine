from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = MenuItem
menus = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
game = True
while game:
    choice = input(f"What would you like? {menus.get_items()}:")
    if choice == "off":
        game = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menus.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink):

            cost = drink.cost
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(drink)








