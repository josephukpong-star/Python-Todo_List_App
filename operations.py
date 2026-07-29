from todo import save_tasks
from datetime import datetime
def view_tasks(tasks):
    """View the task in the to-do list."""
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task["completed"] else "[]"
        print(f"{index}. [{status}] {task['task']}")
def add_task(tasks):
    """Add a new task to the to-do list."""
    new_task = input("Enter a new task: ").strip()
    if new_task:
        tasks.append({"task": new_task, "completed": False})
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")
def complete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    try:
        number = int(input("Enter the task number to mark as completed: "))
        if 1 <= number <= len(tasks):
            if tasks[number - 1]["completed"]:
                  print(f"'{tasks[number - 1]['task']}' has already been completed.")
            else:
               tasks[number - 1]["completed"] = True
               save_tasks(tasks)
               print(f"'{tasks[number - 1]['task']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    try:
        number = int(input("Enter the task number to delete: "))
        if 1 <= number <= len(tasks):
            while True:
                confirm = input(f"Are you sure you want to delete '{tasks[number - 1]['task']}'? (y/n): ").strip().lower()
                if confirm in ("y", "yes"):
                    confirm = "y"
                    break
                elif confirm in ("n", "no"):
                    confirm = "n"
                    break
                print("Please enter y/yes or n/no.")
            if confirm =="y":
                deleted = tasks.pop(number - 1)
                save_tasks(tasks)
                print(f"Task '{deleted['task']}' deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def show_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    if total == 0:
        percentage = 0
    else:
        percentage = (completed / total) * 100
    print("\n===== TASK STATISTICS =====")
    print(f"Total Tasks        : {total}")
    print(f"Completed Tasks    : {completed}")
    print(f"Pending Tasks      : {pending}")
    print(f"Completion Rate    : {percentage:.1f}%")
    if total > 0 and completed == total:
        print("\n🎉 Congratulations!")
        print("All tasks have been completed!")
def search_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    keyword = input("Enter a keyword to search: ").strip().lower()
    if not keyword:
        print("Search keyword cannot be empty.")
        return
    found = False
    print("\n===== SEARCH RESULTS =====")
    for index, task in enumerate(tasks, start=1):
        if keyword in task["task"].lower():
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. [{status}] {task['task']}")
            found = True
    if not found:
        print("No matching tasks found.")
def edit_task(tasks):
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    try:
        number = int(input("Enter the task number to edit: "))
        if 1 <= number <= len(tasks):
            new_name = input("Enter the new task name: ").strip()
            if not new_name:
                print("Task name cannot be empty.")
                return
            old_name = tasks[number - 1]["task"]
            tasks[number - 1]["task"] = new_name
            save_tasks(tasks)
            print(f"Task updated successfully!")
            print(f"'{old_name}' → '{new_name}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def sort_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n===== SORT TASKS =====")
    print("1. Alphabetically (A-Z)")
    print("2. By Completion Status")
    while True:
        choice = input("Choose an option: ")
        if choice in ("1", "2"):
           break
    print("Please choose 1 or 2.")
    if choice == "1":
        tasks.sort(key=lambda task: task["task"].lower())
        save_tasks(tasks)
        print("Tasks sorted alphabetically.")
    elif choice == "2":
        tasks.sort(key=lambda task: task["completed"])
        save_tasks(tasks)
        print("Tasks sorted by completion status.")
    else:
        print("Invalid option.")
        return
    print("\nUpdated Task List:")
    view_tasks(tasks)
def export_tasks(tasks):
    if not tasks:
        print("No tasks available to export.")
        return
    filename = "exported_tasks.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("===== TO-DO LIST =====\n\n")
        for index, task in enumerate(tasks, start=1):
            status = "[X]" if task["completed"] else "[]"
            file.write(f"{index}. [{status}] {task['task']}\n")
    print(f"Tasks exported successfully to '{filename}'.")
def import_tasks(tasks):
    filename = "import_tasks.txt"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            count = 0
            for line in file:
                task = line.strip()         
                if task:
                    exists = any( existing_task["task"].lower() == task.lower()for existing_task in tasks )
                    if exists:
                        print(f"Skipped duplicate task: {task}")
                    else:
                        tasks.append({"task": task, "completed": False })
                        count += 1
        save_tasks(tasks)
        print(f"{count} task(s) imported successfully.")
    except FileNotFoundError:
        print(f"'{filename}' was not found.")
def generate_report(tasks):
    filename = "task_report.txt"
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    current_time = datetime.now()
    with open(filename, "w", encoding="utf-8") as file:
        file.write("===== TASK REPORT =====\n\n")
        file.write(f"Generated: {current_time:%d-%m-%Y %H:%M:%S}\n\n")
        file.write(f"Total Tasks      : {total}\n")
        file.write(f"Completed Tasks  : {completed}\n")
        file.write(f"Pending Tasks    : {pending}\n\n")
        file.write("Task List\n")
        file.write("----------------------\n")
        for index, task in enumerate(tasks, start=1):
            status = "[X]" if task["completed"] else "[]"
            file.write(f"{index}. [{status}] {task['task']}\n")
    print(f"Report generated successfully as '{filename}'.")