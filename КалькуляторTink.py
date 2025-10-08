import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, width=16, font=("Arial", 24), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    else:
        action = lambda x=text: click_button(x)
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="C", width=22, height=2, font=("Arial", 14),
          command=clear_entry).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
