import os

todo_file = "tasks.txt"

def load_tasks():
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as file:
        return [task.strip() for task in file.readlines()]


def save_tasks(tasks):
    with open(todo_file, "w") as file:
        file.writelines([task + "\n" for task in tasks])

def show_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
# Compare this snippet from Medium/To_do_list.py: