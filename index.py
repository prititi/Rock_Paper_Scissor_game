import tkinter as tk
import random

# Function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Scissors" and computer_choice == "Paper")
        or (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "User"
    else:
        return "Computer"

# Function to handle user's choice
def make_choice(choice):
    global user_score, computer_score, draw_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = get_winner(choice, computer_choice)

    if result == "User":
        user_score += 1
    elif result == "Computer":
        computer_score += 1
    else:
        draw_score += 1

    score_label.config(text=f"User: {user_score}\t Computer: {computer_score}\t Draw: {draw_score}")
    result_label.config(text=f"User choice: {choice}\t Computer choice: {computer_choice}\t Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("300x200")

# Create the game labels
score_label = tk.Label(window, text="User: 0\t Computer: 0\t Draw: 0")
score_label.pack()

result_label = tk.Label(window, text="User choice:\t Computer choice:\t Result:")
result_label.pack()

# Create the game buttons
rock_button = tk.Button(window, text="Rock", command=lambda: make_choice("Rock"))
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=lambda: make_choice("Paper"))
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=lambda: make_choice("Scissors"))
scissors_button.pack()

# Initialize the game scores
user_score = 0
computer_score = 0
draw_score = 0

# Start the game
window.mainloop()


