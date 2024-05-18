from tkinter import *
from tkinter import messagebox as mb

wnd = Tk()
wnd.geometry("300x250")
def click():
    print("Привет, ", ent.get())
    mb.showinfo("Информація", "Привет, " + ent.get() + "!")

btn=Button(text="Привет", command=click)
btn.place(x=100, y=120, width=100, height=35)
ent=Entry()
ent.place(x=100, y=60, width=100, height=35)
lb = Label(text="Ваше ім'я:")
lb.place(x=100, y=20, width=100, height=35)

wnd.mainloop()

