from tkinter import *
from PIL import Image, ImageTk
import sqlite3

def selectt(root):
    root.title('Selection')
    root.configure(bg="#ffeff2")  # Light pink background color
    root.geometry("1000x1000")

    def remove():
        import removee
        print("Remove Button Clicked")

    def add():
        import addd
        print("Add Button Clicked")

    def report():
        import report
        print("Generate Button Clicked")

    button_frame = Frame(root, bg="#ffeff2")
    button_frame.place(relx=0.5, rely=0.5, anchor='center')

    button1 = Button(button_frame, text="Remove a dress", bg="#fed3e6", bd=1, relief="solid",
                     command=remove, font=("Papyrus 19 bold"))
    button1.pack(side=LEFT, padx=10)

    button2 = Button(button_frame, text="Add a dress", bg="#fed3e6", bd=1, relief="solid",
                     command=add, font=("Papyrus 19 bold"))
    button2.pack(side=LEFT, padx=10)

    button3 = Button(button_frame, text="Generate report", bg="#fed3e6", bd=1, relief="solid",
                     command=report, font=("Papyrus 19 bold"))
    button3.pack(side=LEFT, padx=10)

    root.mainloop()
