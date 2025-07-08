import tkinter as tk
import threading
import time
import winsound

def fake_process(canvas, root):
    messages = [
        "Подключение к системному ядру...",
        "Удаление системных файлов...",
        "Форматирование диска C:...",
        "Стирание BIOS...",
        "Инициализация перезапуска ядра...",
        "Ошибка! Критическое повреждение системы!",
        "Попытка восстановления...",
        "Восстановление не удалось.",
        "СИСТЕМА УНИЧТОЖЕНА.",
        "ПОДГОТОВКА К ПАДЕНИЮ СИСТЕМЫ...",
    ]
    y = 100
    for msg in messages:
        canvas.create_text(50, y, text=msg, anchor="w", fill="lime", font=("Consolas", 16))
        y += 30
        root.update()
        time.sleep(1.2)

    time.sleep(2)
    show_bsod(root)

def show_bsod(root):
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg="#0078D7")

    try:
        winsound.MessageBeep(winsound.MB_ICONHAND)
    except:
        pass

    bsod_text = """
:(

Your PC ran into a problem and needs to restart.
We're just collecting some error info, and then we'll restart for you.

If you'd like to know more, you can search online later for this error: KERNEL_INITIALIZATION_FAILED
"""
    label = tk.Label(root, text=bsod_text, fg="white", bg="#0078D7",
                     font=("Segoe UI", 18), justify="left")
    label.pack(padx=50, pady=150)

    # Ничего не закрываем — только по Esc
    root.bind("<Escape>", lambda e: root.destroy())

# Главное окно
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.title("Critical System Error")
root.config(cursor="none")

canvas = tk.Canvas(root, bg="black", highlightthickness=0, cursor="none")
canvas.pack(fill="both", expand=True)

threading.Thread(target=fake_process, args=(canvas, root), daemon=True).start()

root.mainloop()
