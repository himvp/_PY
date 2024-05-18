import tkinter as tk
from tkinter import messagebox

# Функция для обработки нажатия кнопки
def on_button_click():
    messagebox.showinfo("Информация", "Кнопка нажата!")

# Создание основного окна
root = tk.Tk()
root.title("Tkinter Button Example")

# Установка размера окна
root.geometry("300x200")

# Создание кнопки и размещение её в центре окна
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.place(x=100, y=60, width=100, height=35)
#button.pack(expand=True)

# Запуск главного цикла обработки событий
root.mainloop()
