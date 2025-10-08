import tkinter as tk
import random
import threading
import time
import os
import winsound

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.title("System Anomaly")
root.config(cursor="none")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

center_dot = canvas.create_oval(
    root.winfo_screenwidth() // 2 - 10,
    root.winfo_screenheight() // 2 - 10,
    root.winfo_screenwidth() // 2 + 10,
    root.winfo_screenheight() // 2 + 10,
    fill="white", outline="")

windows = []
effects_active = True

def move_windows():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    while windows and effects_active:
        for win in windows:
            try:
                x = random.randint(0, screen_width - 300)
                y = random.randint(0, screen_height - 200)
                win.geometry(f"300x200+{x}+{y}")
            except tk.TclError:
                pass
        time.sleep(0.1)

def open_many_windows():
    for _ in range(30):
        win = tk.Toplevel()
        win.attributes("-topmost", True)
        win.geometry("300x200+0+0")
        win.configure(bg="black")
        win.config(cursor="none")

        dot = tk.Canvas(win, width=10, height=10, bg="black", highlightthickness=0)
        dot.place(relx=0.5, rely=0.5, anchor="center")
        dot.create_oval(0, 0, 10, 10, fill="red", outline="")

        win.protocol("WM_DELETE_WINDOW", lambda: None)
        windows.append(win)

    threading.Thread(target=move_windows, daemon=True).start()

def close_all_windows():
    for win in windows:
        try:
            win.destroy()
        except:
            pass
    windows.clear()

def screen_shake():
    original_x = root.winfo_x()
    original_y = root.winfo_y()
    while effects_active:
        dx = random.randint(-15, 15)
        dy = random.randint(-15, 15)
        root.geometry(f"+{original_x + dx}+{original_y + dy}")
        time.sleep(0.1)
    root.geometry(f"+{original_x}+{original_y}")

def matrix_rain():
    chars = "01010101010101010101"
    texts = []
    while effects_active:

        texts = [t for t in texts if canvas.coords(t[0])[1] < root.winfo_screenheight() + 50]
        
        if len(texts) < 80 and random.random() < 0.3:
            x = random.randint(0, root.winfo_screenwidth())
            y = -20
            speed = random.uniform(3, 7)
            char = random.choice(chars)
            text = canvas.create_text(x, y, text=char, 
                                    fill="#ff0000",
                                    font=("Courier", random.randint(10, 16)),
                                    anchor="nw")
            texts.append((text, speed, char))
        
        for i, (text_id, speed, char) in enumerate(texts):
            canvas.move(text_id, 0, speed)
            if random.random() < 0.1:
                new_char = random.choice(chars)
                canvas.itemconfig(text_id, text=new_char)
                texts[i] = (text_id, speed, new_char)
        
        root.update()
        time.sleep(0.03)
    
    for text_id, _, _ in texts:
        canvas.delete(text_id)

def glitch_effects():
    while effects_active:
        if random.random() < 0.2:
            color = random.choice(["red", "white"])
            canvas.configure(bg=color)
            root.update()
            time.sleep(0.05)
            canvas.configure(bg="black")
            root.update()
        
        if random.random() < 0.15:
            x1 = random.randint(0, root.winfo_screenwidth())
            y1 = random.randint(0, root.winfo_screenheight())
            x2 = random.randint(0, root.winfo_screenwidth())
            y2 = y1 + random.randint(5, 20)
            line = canvas.create_line(x1, y1, x2, y2, fill="white", width=2)
            root.update()
            time.sleep(0.1)
            canvas.delete(line)
        
        time.sleep(0.1)

    # os.system("shutdown /r /t 0")

def sequence():
    global effects_active
    
    time.sleep(14)
    canvas.itemconfig(center_dot, fill="red")
    open_many_windows()

    time.sleep(25)
    close_all_windows()
    
    threading.Thread(target=screen_shake, daemon=True).start()
    threading.Thread(target=matrix_rain, daemon=True).start()
    threading.Thread(target=glitch_effects, daemon=True).start()
    
    time.sleep(25)

    effects_active = False

    time.sleep(0.5)
    time.sleep(30)

threading.Thread(target=sequence, daemon=True).start()

winsound.PlaySound("• sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

root.mainloop()