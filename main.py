from ingredients import MENU
from ingredients import resources

#Prompt the user by asking "What would you like?"

# Turn off the coffee machine by entering 'off' to the prompt

def turn_off():
    if user_choice == "off": 
        return False 
    return True

#Print a report showing current resources eg: water, milk, coffee, money
def report(resources, total):
    if user_choice == "report":
        print(resources)
        print(f"Money: ${total: .2f}")

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
    total = (quarters * 0.25 + dimes * 0.10 + nickel * 0.05 + pennies * 0.01)
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
money = 0

while is_on:
    #Prompt the user
    user_choice = input(f"What would you like? {'/'.join(MENU.keys())}: ")

    # Turn machine off
    if user_choice == "off":
        is_on = False
    # Print report
    elif user_choice == "report":
        report(resources, money)

    # make coffee
    elif user_choice in MENU:
        if sufficient_resources():
            payment = process_coins()
            if check_transaction(payment):
                money += MENU[user_choice]["cost"]
                make_coffee()
    else:
        print("Invalid choice. Please choose a drink from the menu. ")


           

    


