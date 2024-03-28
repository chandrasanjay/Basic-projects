# Define a class for the To-Do List
class ToDoList:
    def __init__(self):
        self.tasks = []

    # Method to display the tasks in the to-do list
    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")

    # Method to add a task to the to-do list
    def add_task(self, task_name):
        self.tasks.append({'name': task_name, 'completed': False})
        print(f"Task '{task_name}' added to your to-do list.")

    # Method to mark a task as completed
    def complete_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            self.tasks[task_num - 1]['completed'] = True
            print(f"Task {task_num} marked as completed.")
        else:
            print("Invalid task number.")

    # Method to remove a task from the to-do list
    def remove_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            del self.tasks[task_num - 1]
            print(f"Task {task_num} removed from your to-do list.")
        else:
            print("Invalid task number.")


# Main function to interact with the To-Do List Application
def main():
    todo_list = ToDoList()

    while True:
        print("\nWhat would you like to do?")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter the task name: ")
            todo_list.add_task(task_name)
        elif choice == '3':
            task_num = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(task_num)
        elif choice == '4':
            task_num = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_num)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
