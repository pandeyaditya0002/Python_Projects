import json
import os

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(amount, category, description):
    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category, "description": description})
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    total = 0
    for index, expense in enumerate(expenses, 1):
        print(f"{index}. {expense['category']}: ${expense['amount']} - {expense['description']}")
        total += expense["amount"]
    print(f"\nTotal Expenses: ${total}")


def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted expense: {removed['category']} - ${removed['amount']}")
    else:
        print("Invalid expense number.")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Transport, Bills): ")
            description = input("Enter description: ")
            add_expense(amount, category, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_expenses()
            index = int(input("Enter expense number to delete: ")) - 1
            delete_expense(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
