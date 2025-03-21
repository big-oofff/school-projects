a = True
tasks = []
while a:
    options = ["1. Add a task", "2. View tasks", "3. Remove a task by name", "4. Remove a task by position", "5. Quit"]
    print("Welcome to your To-Do List Manager!")
    print("What would you like to do?")
    for a in options:
        print(a)
    num = int(input("Enter the number of your choice: "))
    if num == 1:
        task = input("Enter the task you want to add: ")
        tasks.append(task)
        print(task + " has been added to your to-do list")
    if num == 2:
        print("Here are your tasks: ")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])
    if num == 3:
        task = input("Enter the name of the task you want to remove: ")
        tasks.remove(task)
        print(task + " has been removed from your to-do list.")
    if num == 4:
        print("Here are your tasks:")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])
        task = int(input("Enter the number of the task you want to remove: "))
        print(tasks[task - 1] + " has been removed from your to-do list.")
        del tasks[task - 1]
    if num == 5:
        print("Goodbye!")
        a = False


            

