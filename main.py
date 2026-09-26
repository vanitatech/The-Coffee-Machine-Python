from ingredients import MENU
from ingredients import resources


#Print a report showing current resources eg: water, milk, coffee, money
def report(resources, total):
    if user_choice == "report":
        print(resources)
        print(f"Profit: ${total: .2f}")

#check if the resouces are sufficient
def sufficient_resources():
    print(f"You have chosen {user_choice}.")
    drink = MENU[user_choice]
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True
#process coins
def process_coins():
    print("Please insert payment.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickel = int(input("How many nickel? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25 + dimes * 0.10 + nickel * 0.05 + pennies * 0.01)
    return total

#check if the transaction is successful
# cost_of_the_drink = 0
def check_transaction(payment_total):
    cost = MENU[user_choice]["cost"]
    print(f"Checking you payment of {payment_total} against cost of {cost}")
    if payment_total == cost:
        print("Transaction successful")
        # cost_of_the_drink += payment_total
        return True
    elif payment_total > cost:
        change = payment_total - cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False
 
#make coffee
def make_coffee():
    print("Making drink now...")
    # todo: reduce resources
    drink = MENU[user_choice]
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient] 
    print(f"Here is your {user_choice}. Enjoy!")

is_on = True
profit = 0

while is_on:
    #Prompt the user
    user_choice = input(f"What would you like? {'/'.join(MENU.keys())}: ")

    # Turn machine off
    if user_choice == "off":
        print("Turning off machine.")
        is_on = False
    # Print report
    elif user_choice == "report":
        report(resources, profit)

    # make coffee
    elif user_choice in MENU:
        if sufficient_resources():
            payment = process_coins()
            if check_transaction(payment):
                profit += MENU[user_choice]["cost"]

                make_coffee()
    else:
        print("Invalid choice. Please choose a drink from the menu. ")


           

    


