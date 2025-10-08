import tkinter as tk
from tkinter import messagebox

current_player = "X"

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Победа!", f"Игрок {current_player} победил!")
            reset_board()
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_winner():
    for i in range(3):
        # строки и столбцы
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    # диагонали
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def reset_board():
    global current_player
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""

root = tk.Tk()
root.title("Крестики-Нолики")
root.geometry("300x350")
root.resizable(False, False)

buttons = [[None for _ in range(3)] for _ in range(3)]

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", width=10, height=4, font=("Arial", 16),
                                  command=lambda row=r, col=c: on_click(row, col))
        buttons[r][c].grid(row=r, column=c)

reset_btn = tk.Button(root, text="Новая игра", font=("Arial", 12), command=reset_board)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=10)

root.mainloop()
