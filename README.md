# Python Coffee Machine

A beginner-friendly Python project that simulates a **coffee machine**. The program allows a user to select a drink, checks whether there are enough ingredients available, processes coins, checks the payment, and prepares the selected coffee.

## Features

* Select a coffee from the available menu
* Check whether enough ingredients are available
* Accept coins as payment
* Calculate the total amount inserted
* Check whether the customer has paid enough
* Calculate and return change
* Refund money when insufficient payment is made
* Includes a function for turning the machine off
* Includes a function for displaying machine resources
* Runs continuously using a `while` loop

## Technologies Used

* **Python 3**
* Functions
* Dictionaries
* `while` loops
* `for` loops
* `if / elif / else` statements
* User input
* Arithmetic calculations
* Imported modules

## Project Structure

```text
Coffee_Machine/
│
├── main.py
├── ingredients.py
└── README.md
```

### `main.py`

Contains the main coffee machine program, including functions for:

* Checking resources
* Processing coins
* Checking transactions
* Making coffee
* Turning the machine off
* Printing a resource report

### `ingredients.py`

Contains the coffee machine's menu and available resources.

For example:

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50
    }
}
```

## How It Works

### 1. Select a drink

The user is prompted to choose a drink from the available menu:

```text
What would you like? espresso/latte/cappuccino:
```

### 2. Check resources

The `sufficient_resources()` function checks whether the machine has enough ingredients to make the selected drink.

```python
if drink["ingredients"][ingredient] > resources[ingredient]:
    print(f"Sorry, there is not enough {ingredient}")
```

If there is not enough of an ingredient, the machine informs the user and stops the transaction.

### 3. Insert coins

The `process_coins()` function asks the user how many coins they are inserting:

```text
How many quarters?
How many dimes?
How many nickel?
How many pennies?
```

The coins are then converted into a total monetary value.

### 4. Check the transaction

The `check_transaction()` function compares the amount inserted with the cost of the selected drink.

If the customer pays the exact amount:

```text
Transaction successful
```

If they pay too much, the machine calculates the change:

```text
Here is $0.50 in change.
```

If they do not pay enough:

```text
Sorry, that's not enough money. Money refunded
```

### 5. Make the coffee

If there are sufficient ingredients and the payment is successful, `make_coffee()` is called:

```text
Here is your latte. Enjoy!
```

## Python Concepts Practised

This project helps practise several important Python concepts:

### Functions

The program is divided into smaller functions, such as:

```python
def sufficient_resources():
```

```python
def process_coins():
```

```python
def check_transaction(total):
```

Breaking the program into functions makes the code easier to understand and maintain.

### Dictionaries

The project uses dictionaries to store menu items, ingredients, prices, and resources.

### Loops

A `while` loop keeps the coffee machine running:

```python
while is_on:
```

A `for` loop is used to check each ingredient required for a drink.

### Conditional Statements

`if`, `elif`, and `else` statements are used to make decisions based on available resources and payment.

### User Input

The `input()` function allows the user to interact with the coffee machine through the terminal.

## How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd Coffee_Machine
```

Run the program:

```bash
python main.py
```

## Future Improvements

Possible improvements to the project include:

* Add the ability to type `off` directly into the main
