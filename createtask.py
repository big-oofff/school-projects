def updateToDo(temptask, tempstatus, tasks):
    if tempstatus == "1":  
        if temptask in tasks:
            del tasks[temptask]
            print(f"Task '{temptask}' completed and removed from the list.")
        else:
            print("Task not found.")
    else:  
        tasks[temptask] = "Incomplete"
    return tasks  

def formatTaskList(tasks):
    task_formatting = ["\nTo-Do LIST", "----------------"]
    if len(tasks) == 0:
        return (0, "No tasks in the list.")
    else:
        for task, status in tasks.items():
            task_formatting.append(f"{task}: {status}")
    task_formatting.append("----------------\n")
    return task_formatting

def main():
    tasks = {}  
    while True:
        print("1. Add/Modify a task")
        print("2. View all tasks")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            status = input("Enter the status: (1 for completed, 0 for incomplete) ")
            tasks = updateToDo(task, status, tasks)
            print("Task list updated.")
            
        elif choice == "2":
            formatted = formatTaskList(tasks)
            if formatted[0] != 0:
                for line in formatted:
                    print(line)
            else:
                print(formatted[1])
        elif choice == "3":
            print("Exiting program. Have a productive day!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()