Tasks=[]

def Task_add():
    task = input("User Add :\n")
    Tasks.append(task)
    return Tasks


def task_show():
    if not Tasks:
        return "Empty Task"
    else:
        return ("\n".join(f"{i}. {task}" for i, task in enumerate(Tasks, start=1)).strip())


def Task_del(): 
    if not Tasks:
        return "No Task Delete"
    try:
        index = int(input("Enter Task Number to Delete: \n"))
        if 0 < index <= len(Tasks):
            removed = Tasks.pop(index-2)
            return f"Task is Deleted {removed}"
        else:
            return "Invalid task"
    except ValueError:
        return "Enter valid Number"
    
while True:
    print("\nOptions: A-Add | B-Show | C-Delete | D-Exit")
    Choose = input("User Choice: ").upper()

    if Choose == "A":
        print(Task_add())
    elif Choose == "B":
        print(task_show())
    elif Choose == "C":
        print(Task_del())
        print(task_show())
    elif Choose == "D":
        print("👋 Exiting... Bye!")
        break
    else:
        print("⚠️ Invalid choice, try again")