import tkinter as tk

def press(key):
    # append digit/operator or clear/evaluate
    if key == "C":
        entry.delete(0, tk.END)
    elif key == "=":
        try:
            entry.insert(tk.END, " = " + str(eval(entry.get())))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, key)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=("Arial", 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

keys = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+'
]

r = 1
c = 0
for k in keys:
    tk.Button(root, text=k, width=4, height=2, font=("Arial",18),
              command=lambda char=k: press(char)) \
      .grid(row=r, column=c, padx=3, pady=3)
    c += 1
    if c > 3:
        c = 0
        r += 1

root.mainloop()


