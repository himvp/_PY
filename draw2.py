import tkinter as tk
from PIL import Image, ImageDraw, ImageGrab

# Функция для сохранения холста как изображения
def save_canvas():
    # Координаты области холста
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # Сохранение изображения области холста
    ImageGrab.grab().crop((x, y, x1, y1)).save("canvas_image.png")
    print("Изображение сохранено как canvas_image.png")

# Создание главного окна
root = tk.Tk()
root.title("Tkinter Canvas Example")

# Создание холста
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

# Рисование фигур на холсте
canvas.create_rectangle(50, 50, 150, 150, fill='blue', outline='black')
canvas.create_oval(200, 50, 300, 150, fill='red', outline='black')
canvas.create_line(50, 200, 350, 200, fill='green', width=5)
canvas.create_text(200, 250, text="Hello, Tkinter!", fill='black')

# Создание кнопки для сохранения изображения
save_button = tk.Button(root, text="Save Canvas", command=save_canvas)
save_button.pack()

# Запуск главного цикла обработки событий
root.mainloop()
