import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    
    if name and phone:
        contacts.append((name, phone))
        listbox.insert(tk.END, name)
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill both name and phone.")

def view_contact(event):
    index = listbox.curselection()
    if index:
        name, phone = contacts[index[0]]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, name)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, phone)

def delete_contact():
    index = listbox.curselection()
    if index:
        contacts.pop(index[0])
        listbox.delete(index)
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)

def search_contact():
    search_term = entry_name.get().lower()
    listbox.delete(0, tk.END)
    for name, phone in contacts:
        if search_term in name.lower():
            listbox.insert(tk.END, name)

# GUI Setup
root = tk.Tk()
root.title("Simple Contact Book")
root.geometry("400x400")

# Name Field
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Phone Field
tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Search", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Contact List
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)
listbox.bind("<<ListboxSelect>>", view_contact)

# Run GUI
root.mainloop()


