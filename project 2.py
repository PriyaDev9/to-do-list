tasks = []

1
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")


def mark_completed():
    view_tasks()
    if tasks:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task marked as completed.")
        else:
            print("Invalid task number.")


def main():
    print("Welcome to the To-Do List App!")
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
