# to_do_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"task": task, "status": "pending"})

    def view_tasks(self):
        """Display all tasks in the list"""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['task']} - {task['status']}")

    def update_task(self, task_number, new_status):
        """Update the status of a task"""
        try:
            task_number = int(task_number)
            if task_number > 0 and task_number <= len(self.tasks):
                if new_status.lower() in ["pending", "done"]:
                    self.tasks[task_number - 1]["status"] = new_status
                    print(f"Task {task_number} updated to {new_status}")
                else:
                    print("Invalid status. Please enter 'pending' or 'done'.")
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_task(self, task_number):
        """Delete a task from the list"""
        try:
            task_number = int(task_number)
            if task_number > 0 and task_number <= len(self.tasks):
                del self.tasks[task_number - 1]
                print(f"Task {task_number} deleted")
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            if not todo_list.tasks:
                print("No tasks in the list.")
            else:
                task_number = input("Enter the task number to update: ")
                new_status = input("Enter the new status (pending/done): ")
                todo_list.update_task(task_number, new_status)
        elif choice == "4":
            if not todo_list.tasks:
                print("No tasks in the list.")
            else:
                task_number = input("Enter the task number to delete: ")
                todo_list.delete_task(task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()