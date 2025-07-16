import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Dice Roll")
root.geometry("300x300")

def game_over(winner_message):
    roll_button.config(state=tk.DISABLED)
    hold_button.config(state=tk.DISABLED)
    play_again = messagebox.askyesno("Game Over", winner_message + "\nPlay Again?")
    if play_again:
        global player_total, computer_total, current_player
        player_total = 0
        computer_total = 0
        current_player = "player"

        player_score_label.config(text="Player Score: 0")
        computer_score_label.config(text="Computer Score: 0")
        message_label.config(text="Would You Like to Roll the Die or End Turn?")

        roll_button.config(state=tk.NORMAL)
        hold_button.config(state=tk.NORMAL)
    else:
        root.destroy()

def player_roll():
    global player_total, current_player

    if current_player != "player":
        return

    roll = random.randint(1, 6)
    if roll == 1:
        message_label.config(text="You Rolled a 1! Turn Over.")
        current_player = "computer"
        roll_button.config(state=tk.DISABLED)
        hold_button.config(state=tk.DISABLED)
        root.after(1000, computer_roll)
    else:
        player_total += roll
        player_score_label.config(text=f"Player Score: {player_total}")
        message_label.config(text=f"You Rolled a {roll}. Roll Again or End Turn?")
        if player_total == 50:
            game_over("You Reached 50! You Win!")
            return
        elif player_total > 50:
            game_over("You Exceeded 50! Computer Wins!")
            return

def player_hold():
    global current_player

    if current_player != "player":
        return

    message_label.config(text=f"You hold at: {player_total}. Computer turn.")
    current_player = "computer"
    roll_button.config(state=tk.DISABLED)
    hold_button.config(state=tk.DISABLED)
    root.after(1000, computer_roll)

def computer_roll():
    global computer_total, current_player, player_total

    roll = random.randint(1, 6)
    if roll == 1:
        message_label.config(text="Computer Rolled a 1! Turn Over.")
        current_player = "player"
        roll_button.config(state=tk.NORMAL)
        hold_button.config(state=tk.NORMAL)
    else:
        computer_total += roll
        computer_score_label.config(text=f"Computer Score: {computer_total}")
        message_label.config(text=f"Computer Rolled a {roll}.")
        if computer_total == 50:
            game_over("Computer Reached 50! Computer Wins!")
            return
        elif computer_total > 50:
            game_over("Computer Exceeded 50! You Win!")
            return
        elif computer_total >= 48:
            computer_hold()
        else:
            root.after(1000, computer_roll)

def computer_hold():
    global current_player

    if computer_total >= 48:
        message_label.config(text=f"Computer Holds at {computer_total}. Player Turn!")
        current_player = "player"
        roll_button.config(state=tk.NORMAL)
        hold_button.config(state=tk.NORMAL)

def main():
    global root, player_score_label, computer_score_label, message_label
    global roll_button, hold_button
    global player_total, computer_total, current_player

    player_score_label = tk.Label(root, text="Player Score: 0")
    player_score_label.pack(pady=10)
    computer_score_label = tk.Label(root, text="Computer Score: 0")
    computer_score_label.pack(pady=10)

    message_label = tk.Label(root, text="Would You Like to Roll the Die or End Turn?")
    message_label.pack(pady=20)

    roll_button = tk.Button(root, text="Roll", width=10, command=player_roll)
    roll_button.pack(pady=5)

    hold_button = tk.Button(root, text="End Turn", width=10, command=player_hold)
    hold_button.pack(pady=5)

    player_total = 0
    computer_total = 0
    current_player = "player"

if __name__ == "__main__":
    main()
    root.mainloop()
