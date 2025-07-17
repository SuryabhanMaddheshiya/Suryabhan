import tkinter as tk
from tkinter import messagebox

def load_tasks():
    try:
        with open("tasks.txt") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as f:
        for i in range(listbox.size()):
            f.write(listbox.get(i) + "\n")
    messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    sel = listbox.curselection()
    if sel:
        listbox.delete(sel)
    else:
        messagebox.showwarning("Warning", "Select a task to remove.")

root = tk.Tk()
root.title("To‑Do List")
root.geometry("300x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=5)
load_tasks()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Remove Task", command=remove_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Save Tasks", command=save_tasks).grid(row=0, column=1, padx=5)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def load_tasks():
    try:
        with open("tasks.txt") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as f:
        for i in range(listbox.size()):
            f.write(listbox.get(i) + "\n")
    messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    sel = listbox.curselection()
    if sel:
        listbox.delete(sel)
    else:
        messagebox.showwarning("Warning", "Select a task to remove.")

root = tk.Tk()
root.title("To‑Do List")
root.geometry("300x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=5)
load_tasks()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Remove Task", command=remove_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Save Tasks", command=save_tasks).grid(row=0, column=1, padx=5)

root.mainloop()




