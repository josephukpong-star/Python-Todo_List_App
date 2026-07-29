from todo import load_tasks, save_tasks
from operations import (view_tasks, add_task, complete_task, delete_task, show_statistics, search_tasks, edit_task, sort_tasks, export_tasks, import_tasks, generate_report )
from utils import print_header
tasks = load_tasks()
while True:
    print_header("TO-DO LIST")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Show Task Statistics")
    print("6. Search Tasks")
    print("7. Edit Task")
    print("8. Sort Tasks")
    print("9. Export Tasks")
    print("10. Import Tasks")
    print("11. Generate Report")
    print("12. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
       view_tasks(tasks)
    elif choice == "2":
       add_task(tasks)
    elif choice == "3":
       complete_task(tasks)
    elif choice == "4":
       delete_task(tasks)
    elif choice == "5":
       show_statistics(tasks)
    elif choice == "6":
       search_tasks(tasks)
    elif choice == "7":
       edit_task(tasks)
    elif choice == "8":
       sort_tasks(tasks)
    elif choice == "9":
       export_tasks(tasks)
    elif choice == "10":
       import_tasks(tasks)
    elif choice == "11":
       generate_report(tasks)
    elif choice == "12":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")