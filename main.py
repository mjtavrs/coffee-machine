# Money standard value
QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

# Coffee Menu
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18, }, "cost": 1.5, },
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24, }, "cost": 2.5, },
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24, }, "cost": 3.0, }
}

# Machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Calculates how much money the user has put on the machine
def customer_money(quarters, dimes, nickles, pennies):
    total = ((QUARTER * quarters) + (DIME * dimes) + (NICKLE * nickles) + (PENNY * pennies))
    return total


# Check which option was chose by the user
def user_choice(choice, resources_list, machine_money):
    if choice == 'report':
        water = resources_list["water"]
        milk = resources_list["milk"]
        coffee = resources_list["coffee"]
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${machine_money}")
    elif choice == 'off':
        quit()
    elif choice != 'espresso' and choice != 'latte' and choice != 'cappuccino':
        print("Invalid choice! Try again.")
    else:
        return 1


# Check the resources for the normal machine operation
def check_resources(resources_list, coffee_choice, menu):
    # Created the variables for checking the resources
    water = resources_list['water']
    milk = resources_list['milk']
    coffee = resources_list['coffee']
    for key in menu:
        # Created a flag for checking all resources, not one only
        flag = True
        if coffee_choice == key:
            if water < menu[key]['ingredients']['water']:
                print("Sorry, there's not enough water.")
                flag = False
            if coffee_choice != 'espresso':
                if milk < menu[key]['ingredients']['milk']:
                    print("Sorry, there's not enough milk.")
                    flag = False
            if coffee < menu[key]['ingredients']['coffee']:
                print("Sorry, there's not enough coffee.")
                flag = False
            if flag:
                return 1


# Checks if the user has put enough money for the coffee in the machine
def check_money(customer_total, coffee_choice, menu):
    for key in menu:
        if coffee_choice == key:
            if customer_total < menu[key]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                return 1


# Updating all resources for future orders
def update_resources(resource_list, menu, coffee_choice):
    for key in menu:
        if coffee_choice == key:
            resource_list['water'] -= menu[key]['ingredients']['water']
            # Espressos do not take milk
            if coffee_choice != 'espresso':
                resource_list['milk'] -= menu[key]['ingredients']['milk']
            resource_list['coffee'] -= menu[key]['ingredients']['coffee']


# Starting the Coffee Machine
def coffee_machine():
    """Main function for the Coffee Machine"""
    # Every machine starts without money, and creating a flag for the loop
    machine_money = 0
    start_sell = True

    while start_sell:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        sell = user_choice(choice, resources, machine_money)
        if sell == 1:
            resources_ok = check_resources(resources, choice, MENU)
            if resources_ok == 1:
                print("Please insert coins.")
                c_quarters = float(input("How many quarters?: "))
                c_dimes = float(input("How many dimes?: "))
                c_nickles = float(input("How many nickles?: "))
                c_pennies = float(input("How many pennies?: "))
                total = customer_money(c_quarters, c_dimes, c_nickles, c_pennies)
                money_ok = check_money(total, choice, MENU)
                if money_ok == 1:
                    for key in MENU:
                        if choice == key:
                            change = float(MENU[key]['cost'] < total)
                            print(f"Here's your ${change} in change.")
                            # Every time an order has been taken, the machine keeps the money but not the change
                            machine_money += MENU[key]['cost']
                    print(f"Here's your {choice} ☕. Enjoy!")

                update_resources(resources, MENU, choice)


coffee_machine()
