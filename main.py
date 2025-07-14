import json
import os

File= "tasks.json"

#load tasks from a JSON file
def load_tasks():
    if not os.path.exists(File):
        return []
    with open(File, 'r') as file:
        return json.load(file)

#save tasks to a JSON file    
def save_tasks(tasks):
    with open(File, 'w') as file:
        json.dump(tasks, file, indent=4)

def menu():
    print("To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as done")
    print("4. Remove Task")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks, start=1):
                    status = "✔" if task['done'] else "❌"
                    print(f"{i}. {task['task']} - {status}")
        
        elif choice == '2':
            task_name = input("Enter the task name: ")
            tasks.append({"task": task_name, "done": False})
            save_tasks(tasks)
            print("Task added successfully.")
        
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]['done'] = True
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        
        elif choice == '4':
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                save_tasks(tasks)
                print("Task removed successfully.")
            else:
                print("Invalid task number.")
        
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if  __name__ == "__main__":
    main()