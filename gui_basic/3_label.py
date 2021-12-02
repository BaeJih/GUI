from os import path
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label1 = Label(root, text="안녕하세요")
Label1.pack()

photo = PhotoImage(file="gui_basic/image.png")
Label2 = Label(root, image=photo)
Label2.pack()


def change():
    Label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="gui_basic/image2.png")
    Label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
