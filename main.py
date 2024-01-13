import random
from tkinter import Tk, Label, Button, StringVar, messagebox

exit_game = False
user_points = 0
computer_points = 0

def play_game(user_input):
    global user_points, computer_points

    options = ["rock", "paper", "scissors"]
    computer_input = random.choice(options)

    result_message = f"Your input is {user_input}\nComputer input is {computer_input}\n"

    if user_input == "rock":
        if computer_input == "rock":
            result_message += "It's a tie!"
        elif computer_input == "paper":
            result_message += "Computer wins"
            computer_points += 1
        elif computer_input == "scissors":
            result_message += "You win"
            user_points += 1
    elif user_input == "paper":
        if computer_input == "rock":
            result_message += "You win!"
            user_points += 1
        elif computer_input == "paper":
            result_message += "It's a tie!"
        elif computer_input == "scissors":
            result_message += "Computer wins"
            computer_points += 1
    elif user_input == "scissors":
        if computer_input == "rock":
            result_message += "Computer wins!"
            computer_points += 1
        elif computer_input == "paper":
            result_message += "You win"
            user_points += 1
        elif computer_input == "scissors":
            result_message += "It's a tie"

    messagebox.showinfo("Game Result", result_message)

def on_button_click(choice):
    if choice.lower() == "exit":
        messagebox.showinfo("Game Ended", f"You won a total score of {user_points} and the computer total score is {computer_points}")
        root.destroy()
    elif choice.lower() in ["rock", "paper", "scissors"]:
        play_game(choice)
    else:
        messagebox.showwarning("Invalid Input", "Invalid choice. Please choose rock, paper, scissors, or exit.")

root = Tk()
root.title("Rock-Paper-Scissors Game")

# Label
Label(root, text="Choose rock, paper, scissors, or exit:", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=4, pady=10)

# User Buttons
Button(root, text="Rock", command=lambda: on_button_click("rock"), width=10, height=2).grid(row=1, column=0, padx=5, pady=5)
Button(root, text="Paper", command=lambda: on_button_click("paper"), width=10, height=2).grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Scissors", command=lambda: on_button_click("scissors"), width=10, height=2).grid(row=1, column=2, padx=5, pady=5)
Button(root, text="Exit", command=lambda: on_button_click("exit"), width=10, height=2).grid(row=1, column=3, padx=5, pady=5)



root.mainloop()
