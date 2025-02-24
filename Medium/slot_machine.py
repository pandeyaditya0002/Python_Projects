#

def deposit():
    while True:
        amount =int(input("What would you like to deposite ?"))
        if amount.isdigit():
            amount = int(amount)

