import os

# File to store tasks
TODO_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file"""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks():
    """Display all tasks"""
    tasks = load_tasks()
    if not tasks:
        print("\n✅ No tasks available! Add new tasks. ✅")
    else:
        print("\n📌 To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task"""
    task = input("Enter new task: ").strip()
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Task '{task}' added successfully!")

def delete_task():
    """Delete a task"""
    show_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"❌ Task '{removed_task}' deleted successfully!")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def complete_task():
    """Mark a task as completed"""
    show_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = "✔️ " + tasks[num - 1]
            save_tasks(tasks)
            print(f"🎉 Task marked as completed!")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def main():
    while True:
        print("\n📋 To-Do List Menu")
        print("1️⃣ View Tasks")
        print("2️⃣ Add Task")
        print("3️⃣ Delete Task")
        print("4️⃣ Mark Task as Completed")
        print("5️⃣ Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("👋 Exiting To-Do List. Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
