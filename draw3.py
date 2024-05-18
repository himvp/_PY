#import tkinter as tk
from  tkinter import *

# Создание главного окна
root = Tk()
root.title("Canvas Draw")

root.geometry("400x550")

# Создание холста
canvas = Canvas(root, width=400, height=300, bg='white')
canvas.pack()

# Рисование фигур на холсте
canvas.create_rectangle(50, 50, 150, 150, fill='blue', outline='black')
canvas.create_oval(200, 50, 300, 150, fill='red', outline='black')
canvas.create_line(50, 200, 350, 200, fill='green', width=5)
canvas.create_text(200, 250, text="Hello, Canvas!", fill='black')

cat = PhotoImage(file='cat.png')
# canvas.create_image( 55, 55, anchor=NW, image=cat )

def showimage():   
    # cat = PhotoImage(file='cat.png')
    canvas.create_image( 0, 0, anchor=NW, image=cat )
    label.config(image=cat)
    label.image = cat

# Создание кнопки для сохранения изображения
save_button = Button(root, text="Load Image", command=showimage )
save_button.place(x=100, y=100, width=100, height=35)
save_button.pack()

# Создание метки для отображения изображения
label = Label(root)
label.place(x=50, y=50, width=145, height=145)
label.pack()

# Запуск главного цикла обработки событий
root.mainloop()
