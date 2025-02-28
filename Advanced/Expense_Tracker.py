import json
import os

# Load expenses from the JSON file
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return []

# Save expenses to the JSON file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense to the list and save it
def add_expense(amount, category, description):
    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category, "description": description})
    save_expenses(expenses)
    print("Expense added successfully!")

# View all expenses and print the total amount
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

# Delete an expense by its index and save the updated list
def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted expense: {removed['category']} - ${removed['amount']}")
    else:
        print("Invalid expense number.")

# Main function to run the expense tracker program
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

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()