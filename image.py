import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Функция для загрузки изображения
def load_image():
    # Открыть диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename()
    if file_path:
        # Загрузить изображение и преобразовать его в формат, пригодный для Tkinter
        image = Image.open(file_path)
        image = ImageTk.PhotoImage(image)
        
        # Обновить метку для отображения изображения
        label.config(image=image)
        label.image = image

# Создание главного окна
root = tk.Tk()
root.title("Image Loader")

# Создание кнопки для загрузки изображения
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

# Создание метки для отображения изображения
label = tk.Label(root)
label.pack()

# Запуск главного цикла обработки событий
root.mainloop()
