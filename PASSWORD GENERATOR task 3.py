import tkinter as tk
import random
import string

def generate():
    pw = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    result.delete(0, tk.END)
    result.insert(0, pw)

root = tk.Tk()
tk.Label(root, text="Password:").pack()
result = tk.Entry(root, width=20)
result.pack()
tk.Button(root, text="Generate", command=generate).pack()
root.mainloop()


