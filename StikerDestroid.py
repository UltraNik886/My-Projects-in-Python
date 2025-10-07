import tkinter as tk
import winsound

def main():
    root = tk.Tk()
    root.attributes("-fullscreen", True)   # полноэкранный режим
    root.configure(bg="black")
    root.config(cursor="none")             # скрыть курсор

    # Основная надпись
    label = tk.Label(
        root,
        text="УДАЛИ СТИКЕРЫ",
        font=("Arial", 80, "bold"),
        fg="red",
        bg="black"
    )
    label.pack(expand=True)

    # Таймер ниже текста
    timer_label = tk.Label(
        root,
        text="10:00",
        font=("Arial", 50, "bold"),
        fg="white",
        bg="black"
    )
    timer_label.pack(pady=50)

    # Звук при старте
    winsound.PlaySound("Slaughterhouse.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    # Логика таймера
    def countdown(time_left):
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        if time_left > 0:
            root.after(1000, countdown, time_left - 1)

    countdown(10 * 60)  # 10 минут в секундах

    # Выход только по ESC
    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    main()
