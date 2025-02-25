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
