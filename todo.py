import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return f.read().splitlines()

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        f.write("\n".join(tasks))

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks) and not tasks[index].startswith("✔️"):
        tasks[index] = "✔️ " + tasks[index]
        save_tasks(tasks)
