import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6)]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != " ":
            buttons[combo[0]].config(bg="lightgreen")
            buttons[combo[1]].config(bg="lightgreen")
            buttons[combo[2]].config(bg="lightgreen")
            messagebox.showinfo("Game Over", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

def on_button_click(i):
    global winner
    if buttons[i]['text'] == " " and not winner:
        buttons[i]["text"] = current_player
        check_winner()
        if not winner:
            switch_player()

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic Tac Toe")

def reset_game():
    global current_player, winner
    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace")
    current_player = "X"
    winner = False
    label.config(text="Player X's turn")

buttons = [tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i: on_button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

label = tk.Label(root, text="Player X's turn", font=('normal', 20))
label.grid(row=3, column=0, columnspan=3)
current_player = "X"
winner = False

reset_button = tk.Button(root, text="Reset Game", font=('normal', 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()