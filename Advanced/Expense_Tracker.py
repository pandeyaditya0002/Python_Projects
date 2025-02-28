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
        
