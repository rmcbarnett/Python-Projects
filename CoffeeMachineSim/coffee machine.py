# Used an OOP approach to build a simulation of a coffee machine. The machine, askes what the user would like, and creates the drink if its available. 
# Of course you have to pay for it first though lol. Change will be made as well from the money machine object.. 

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



money_machine.report()



choice = input(f"What would you like? ({menu.get_items()}):")
while choice != 'off':
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
       drink = menu.find_drink(choice)
       if drink is not None:
           can_drink_be_made = coffee_maker.is_resource_sufficient(drink)
           if can_drink_be_made:
               if money_machine.make_payment(drink.cost):
                   coffee_maker.make_coffee(drink)

    choice = input(f"What would you like? {menu.get_items()} :")


