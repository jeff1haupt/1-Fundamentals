""" 

NOTE TO INSTRUCTORS ABOUT BONUS TASKS 

The solutions for the bonus tasks in this assignment are possible implementations of the bonus tasks.
They are not necessarily the only way. Students may approach the tasks in a different way.
Please bear this in mind :)


"""
from banking_pkg import account


""" Task 1: Student will download and unzip the workshop2 folder.
This folder will contain all the files for this workshop, and the app.py
file will contain the atm_menu function below.
"""


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


"""
Task 2: Register the user's name and PIN. 
"""
print("          === Automated Teller Machine ===          ")
while True:                 # Bonus 1
    name = input("Enter name to register: ")
    if len(name) > 10:
        print("The maximum name length is 10 characters.")
    elif len(name) == 0:
        print("You must enter a name.")
    else:
        break

while True:                 # Bonus 2
    pin = input("Enter PIN: ")
    if len(pin) > 4 or len(pin) < 4:
        print("PIN must contain 4 numbers")
    else:
        break

balance = 0
print(name, "has been registered with a starting balance of $" + str(balance))


"""
Task 3: Log in the user, or deny if PIN is invalid
"""
while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!\n")
        break
    print("Invalid credentials!\n")


"""
Task 3-5: Displays ATM menu and responds to user choice
"""
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":               # balance
        account.show_balance(balance)
    elif option == "2":             # deposit
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":             # withdraw
        balance = account.withdraw(balance)
        account.show_balance(balance)
    else:                           # logout
        account.logout(name)
        break
