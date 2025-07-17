import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    comp_choice = random.choice(choices)
    result = ""
    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    lbl_result.config(text=f"You: {user_choice}   CPU: {comp_choice}\n{result}")

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Buttons
for idx, choice in enumerate(choices):
    btn = tk.Button(root, text=choice, width=10,
                    command=lambda c=choice: play(c))
    btn.grid(row=0, column=idx, padx=5, pady=5)

# Result label
lbl_result = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))
lbl_result.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()

