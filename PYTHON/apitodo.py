import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        
        self.entry = tk.Entry(root)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks)
        self.show_button.pack()

    def add_task(self):
        task = self.entry.get()
        self.tasks.append(task)
        self.entry.delete(0, tk.END)
        messagebox.showinfo("Task Added", f"Task '{task}' added.")

    def remove_task(self):
        task = self.entry.get()
        if task in self.tasks:
            self.tasks.remove(task)
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Task Removed", f"Task '{task}' removed.")
        else:
            messagebox.showerror("Error", f"Task '{task}' not found.")

    def show_tasks(self):
        tasks_text = "\n".join(self.tasks) if self.tasks else "No tasks in the list."
        messagebox.showinfo("Tasks", tasks_text)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
