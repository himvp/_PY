from tkinter import *
root = Tk()
root.title("Draw Cat")
root.geometry("400x300")
canvas = Canvas(root, width=400, height=300, bg='white')
canvas.pack()
cat = PhotoImage(file='cat.png')
canvas.create_image( 0, 0, anchor=NW, image=cat )
root.mainloop()
