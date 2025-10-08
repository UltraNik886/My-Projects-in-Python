import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.config(cursor="none")
root.title("Моя программа")
label = tk.Label(root, text=".", font=("Arial", 50))
label.pack()
root.mainloop()