tasks = []

def add_tasks(task):
    tasks.append(task)

def remove_tasks(task_num):
    if task_num < 0:
        print("Invaled Number!!")
    else:
        tasks.pop(task_num - 1)

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=0):
            print(f"{i}. {task}")

    with open("ToDo.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

print("Welcome to SA To-Do List App.")

while True:

    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter your task: ")
        add_tasks(task)

    elif choice == '2':
        task_num = int(input("Enter task number to remove: "))
        remove_tasks(task_num)

    elif choice == '3':
        view_tasks()

    elif choice == '4':
        print("Exiting App...")
        break

    else:
        print("Invalid Input. Enter correct choice...")
