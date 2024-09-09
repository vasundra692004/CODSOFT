import tkinter as tk
from tkinter import messagebox, Toplevel

class Todo:
    def __init__(self):
        self.Tasks = []

    def add_task(self, task):
        self.Tasks.append(task)

    def remove_task(self, task):
        if task in self.Tasks:
            self.Tasks.remove(task)

    def update_task(self, old_task, new_task):
        if old_task in self.Tasks:
            index = self.Tasks.index(old_task)
            self.Tasks[index] = new_task

    def display_tasks(self):
        tasks = "\n".join(self.Tasks)
        return tasks

class TodoApp:
    def __init__(self, root):
        self.todo = Todo()
        self.root = root
        self.root.title("ToDo List App")

        self.task_label = tk.Label(self.root, text="", justify=tk.LEFT)
        self.task_label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.open_remove_window)
        self.remove_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.open_update_window)
        self.update_button.pack()

        self.display_tasks()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.todo.add_task(task)
            self.entry.delete(0, tk.END)
            self.display_tasks()

    def open_remove_window(self):
        self.remove_window = Toplevel(self.root)
        self.remove_window.title("Remove Task")

        self.remove_task_label = tk.Label(self.remove_window, text="Task Name")
        self.remove_task_label.pack()
        self.remove_task_entry = tk.Entry(self.remove_window)
        self.remove_task_entry.pack()

        self.remove_confirm_button = tk.Button(self.remove_window, text="Remove Task", command=self.remove_task)
        self.remove_confirm_button.pack()

    def remove_task(self):
        task = self.remove_task_entry.get()
        if task:
            if task in self.todo.Tasks:
                self.todo.remove_task(task)
                self.display_tasks()
                self.remove_window.destroy()
            else:
                messagebox.showerror("Error", "Task not found")
        else:
            messagebox.showerror("Error", "Task name cannot be empty")

    def open_update_window(self):
        self.update_window = Toplevel(self.root)
        self.update_window.title("Update Task")

        self.old_task_label = tk.Label(self.update_window, text="Old Task Name")
        self.old_task_label.pack()
        self.old_task_entry = tk.Entry(self.update_window)
        self.old_task_entry.pack()

        self.new_task_label = tk.Label(self.update_window, text="New Task Name")
        self.new_task_label.pack()
        self.new_task_entry = tk.Entry(self.update_window)
        self.new_task_entry.pack()

        self.update_confirm_button = tk.Button(self.update_window, text="Update Task", command=self.update_task)
        self.update_confirm_button.pack()

    def update_task(self):
        old_task = self.old_task_entry.get()
        new_task = self.new_task_entry.get()
        if old_task and new_task:
            if old_task in self.todo.Tasks:
                self.todo.update_task(old_task, new_task)
                self.display_tasks()
                self.update_window.destroy()
            else:
                messagebox.showerror("Error", "Old task not found")
        else:
            messagebox.showerror("Error", "Both fields must be filled")

    def display_tasks(self):
        tasks = self.todo.display_tasks()
        self.task_label.config(text=tasks)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
