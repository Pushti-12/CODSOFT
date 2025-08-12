# Optimized and unique variable naming To-Do List (No Emojis)

todo_items = []  # Stores tasks as tuples (name, is_completed)

def display_list():
    if not todo_items:
        print("\nNo tasks available.\n")
        return
    print("\nCurrent Tasks:")
    for idx, (task_name, is_done) in enumerate(todo_items, start=1):
        status = "[Completed]" if is_done else "[Pending]"
        print(f"{idx}. {task_name} — {status}")
    print()

def add_item():
    task_name = input("Enter task: ").strip()
    if task_name:
        todo_items.append((task_name, False))
        print("Task added!\n")
    else:
        print("Task cannot be empty.\n")

def complete_item():
    if not todo_items:
        print("\nNo tasks to update.\n")
        return
    display_list()
    try:
        index = int(input("Task number to complete: ")) - 1
        if 0 <= index < len(todo_items):
            task_name, _ = todo_items[index]
            todo_items[index] = (task_name, True)  # Update tuple
            print("Task marked completed!\n")
        else:
            print("Invalid index.\n")
    except ValueError:
        print("Enter a valid number.\n")

def remove_item():
    if not todo_items:
        print("\nNo tasks to remove.\n")
        return
    display_list()
    try:
        index = int(input("Task number to delete: ")) - 1
        if 0 <= index < len(todo_items):
            removed_task = todo_items.pop(index)
            print(f"'{removed_task[0]}' removed!\n")
        else:
            print("Invalid index.\n")
    except ValueError:
        print("Enter a valid number.\n")

def menu():
    while True:
        print("===== TO-DO MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            display_list()
        elif choice == "2":
            add_item()
        elif choice == "3":
            complete_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
