import json
import os

TASK_FILE = "task.json"
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,'r') as file:
            return json.load(file)['tasks']
    else:
        return []
def save_tasks(tasks):
    with open(TASK_FILE,'w') as file:
        json.dump({'tasks':tasks},file,indent=4)
def display_tasks(tasks):
    if not tasks:
        print("Your To-Do List is empty.")
        return
    print("Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task['status'] == 'completed' else " ❌"
        print(f"{i}. [{status}] {task['task']}")
def add_task(tasks):
    task_name = input("Enter task name:")
    tasks.append({"task":task_name, "status":"pending"})
    save_tasks(tasks)
    print(f'Task"{task_name}" added successfully.')
def mark_task_as_done(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number:")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['status'] = 'completed'
        save_tasks(tasks)
        print(f'Task "{tasks[task_number]["task"]}" marked as completed. ')
    else:
        print("Invalid task number.")
def remove_tasks(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number:")) - 1
    if 0  <= task_number < len(tasks):
        removed_tasks = tasks.pop(task_number)
        save_tasks(tasks)
        print(f'Task "{removed_tasks["task"]}" removed successfully.')
    else:
            print("Invalid task number.")
def main():
    tasks  = load_tasks()
    while True:
        print("\n Welcome to To-Do List Manager!")
        print("1.Add a task")
        print("2.view all tasks")
        print("3.Mark as task as done")
        print("4.Remove a task")
        print("5.Exit")
        choice = input("Enter your choice:")
        if choice ==  "1":
            add_task(tasks)
        elif choice =="2":
            display_tasks(tasks)
        elif choice == "3":
            mark_task_as_done(tasks)
        elif choice == "4":
            remove_tasks(tasks)
        elif choice == "5":
            print("Gooodbye!")
            break
        else:
            print("Invalid choice.please try again.")
if __name__ == "__main__":
    main()
    












