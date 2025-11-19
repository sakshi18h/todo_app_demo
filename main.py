import sys

tasks = []

def show_menu():
    print("\n--- To-Do List App ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nYour list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if _name_ == "_main_":
    main()