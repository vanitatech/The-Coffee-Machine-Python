# ☕ Python Coffee Machine

A Python-based coffee machine simulator that allows users to select drinks, check available resources, make payments using coins, receive change, and view the machine's current status.

This project was created as part of my **100 Days of Code – Python Bootcamp** to practise writing functions, working with dictionaries, loops, conditionals, user input, and managing program state.

## Features

* Select a coffee from the available menu
* Check whether enough ingredients are available
* Accept different coin denominations
* Calculate the total payment
* Calculate and return change
* Refund insufficient payments
* Display the machine's current resources
* Track money collected from successful purchases
* Turn the coffee machine off
* Handle invalid drink selections
* Keep the machine running until the user chooses to turn it off

## Technologies Used

* **Python 3**
* Functions
* Dictionaries
* `while` loops
* `for` loops
* `if / elif / else` statements
* User input
* Arithmetic operations
* Imported Python modules

## Project Structure

```text
Coffee_Machine/
│
├── main.py
├── ingredients.py
└── README.md
```

### `main.py`

Contains the main coffee machine program and functions for:

* Turning the machine off
* Displaying a report
* Checking available resources
* Processing coins
* Checking payments
* Making coffee

### `ingredients.py`

Contains the coffee machine's menu and available resources.

The menu stores information such as:

* Drink name
* Ingredients required
* Drink price

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

## How to Use

When the program starts, it asks:

```text
What would you like? espresso/latte/cappuccino:
```

### Select a drink

Enter one of the available menu options:

```text
espresso
latte
cappuccino
```

The program checks whether there are enough ingredients before asking for payment.

### Make a payment

The machine asks for the number of each type of coin:

```text
How many quarters?
How many dimes?
How many nickel?
How many pennies?
```

The program calculates the total amount inserted.

### Receive change

If the customer pays more than the drink costs, the machine calculates the change:

```text
Here is $0.50 in change.
```

### Insufficient payment

If the customer does not insert enough money:

```text
Sorry, that's not enough money. Money refunded
```

### View the report

Enter:

```text
report
```

The machine displays its current resources and money collected.

Example:

```text
{'water': 300, 'milk': 200, 'coffee': 100}
Money: $2.50
```

### Turn off the machine

Enter:

```text
off
```

The program stops running.

## Python Concepts Practised

### Functions

The program is divided into separate functions, making each part of the coffee machine easier to understand and manage.

Examples:

```python
def sufficient_resources():
```

```python
def process_coins():
```

```python
def check_transaction(total):
```

```python
def make_coffee():
```

### Dictionaries

Nested dictionaries are used to store the coffee menu, ingredients, prices, and resources.

### Loops

A `while` loop keeps the coffee machine running:

```python
while is_on:
```

A `for` loop checks each ingredient required for a drink.

### Conditional Logic

The program uses `if`, `elif`, and `else` statements to handle:

* Machine shutdown
* Reports
* Drink selection
* Resource availability
* Payment validation
* Invalid input

### Return Values

Functions such as `turn_off()` and `sufficient_resources()` return values that allow the main program to make decisions.

For example:

```python
return False
```

or:

```python
return True
```

### User Input

The `input()` function allows the user to interact with the coffee machine through the terminal.

## Program Flow

```text
Start
  ↓
Ask user what they would like
  ↓
Is it "off"?
  ├── Yes → Turn machine off
  └── No
       ↓
Is it "report"?
  ├── Yes → Display resources and money
  └── No
       ↓
Is it a valid drink?
  ├── No → Display invalid choice
  └── Yes
       ↓
Check resources
  ↓
Enough resources?
  ├── No → Display insufficient resources
  └── Yes
       ↓
Process coins
  ↓
Check payment
  ├── Not enough → Refund money
  └── Enough → Calculate change
                ↓
             Make coffee
                ↓
              Repeat
```

## Future Improvements

Possible improvements for this project include:

* Deduct ingredients from the resources after making each coffee
* Fix the money tracking so the transaction function updates the machine's balance correctly
* Improve input validation for non-numeric coin entries
* Handle invalid menu selections more robustly
* Add a function specifically for updating resources
* Add tests for individual functions
* Improve the report formatting
* Add more drinks to the menu
* Add support for different payment methods

## What I Learned

This project helped me practise breaking a larger program into smaller functions and using those functions together to create a complete application.

I also gained more experience with **Python dictionaries, nested dictionaries, loops, conditional statements, return values, user input, arithmetic calculations, and variable scope**.

The project is part of my ongoing Python learning journey and contributes to my software engineering portfolio.

