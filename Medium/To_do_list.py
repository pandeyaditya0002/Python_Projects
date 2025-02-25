import os

todo_file = "tasks.txt"

def load_tasks():
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as file:
        return [task.strip() for task in file.readlines()]