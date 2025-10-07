import tkinter as tk
import winsound

def main():
    root = tk.Tk()
    root.attributes("-fullscreen", True)   # полноэкранный режим
    root.configure(bg="black")
    root.config(cursor="none")             # скрыть курсор

    label_big = tk.Label(
        root,
        text="УДАЛИ СТИКЕРЫ",
        font=("Arial", 100, "bold"),
        fg="red",
        bg="black"
    )
    label_big.pack(pady=50)

    label_small = tk.Label(
        root,
        text="Я ТЕБЯ ВЗЛОМАЛ!\n"
             "ФАЙЛЫ ДИСТАНЦИОННОГО УПРАВЛЕНИЯ УЖЕ В СИСТЕМЕ,\n"
             "У ТЕБЯ 10 МИНУТ!!!\n"
             "НЕ УДАЛИШЬ СТИКЕРЫ, ВСЕ ДАННЫЕ С ПК БУДУТ УДАЛЕНЫ!!!\n"
             "\n"
             "ХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХА\n"
             "ХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХА\n"
             "ХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХА\n"
             "ХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХА",
        font=("Arial", 40, "bold"),
        fg="red",
        bg="black",
        justify="center"
    )
    label_small.pack(pady=5)

    timer_label = tk.Label(
        root,
        text="10:00",
        font=("Arial", 100, "bold"),
        fg="red",
        bg="black"
    )
    timer_label.pack(pady=90)

    winsound.PlaySound("Slaughterhouse.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    def countdown(time_left):
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        if time_left > 0:
            root.after(1000, countdown, time_left - 1)

    countdown(10 * 60)
    root.mainloop()

if __name__ == "__main__":
    main()
