class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed:", task)
        else:
            print("Task not found:", task)

    def show_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the list.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
