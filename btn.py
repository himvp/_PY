from tkinter import *

def on_button_click():
    print("Информация", "Кнопка нажата!")

root = Tk()
button = Button(root, text="Нажми меня", command=on_button_click)
button.pack()
root.mainloop()