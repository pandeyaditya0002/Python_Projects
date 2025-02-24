#

def deposit():
    while True:
        amount = input("What would you like to deposite ?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print()
        else:
            print("P")


