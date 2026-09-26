from ingredients import MENU
from ingredients import resources

#Prompt the user by asking "What would you like?"

# Turn off the coffee machine by entering 'off' to the prompt
def turn_off():
    off = False
    maintenance = input("Type off to turn the machine off: ")
    if maintenance == "off":
        off = True
        return
#Print a report showing current resources eg: water, milk, coffee, money
def print_report(resources, check_transaction):
    return

#check if the resouces are sufficient
def sufficient_resources():
    drink = MENU[user_choice]
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True
#process coins
def process_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickel = int(input("How many nickel? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickel * 0.05 + pennies * 0.01
    return total
#check if the transaction is successful

cost_of_the_drink = 0
def check_transaction(total):
    cost = MENU[user_choice]["cost"]
    if total == cost:
        print("Transaction successful")
        cost_of_the_drink += total
        return True
    elif total > cost:
        change = total-cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False
 
#make coffee
def make_coffee():
    print(f"Here is your {user_choice}. Enjoy!")

is_on = True

while is_on:
    #Prompt the user by asking "What would you like?"
    user_choice = input(f"What would you like? {'/'.join(MENU.keys())}: ")
    if sufficient_resources():
        total = process_coins()
        if check_transaction(total):
            make_coffee()


