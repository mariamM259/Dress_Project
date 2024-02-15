import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg


def remove_dress(id):
    # Fetching dress ID from the entry

    # dress_id = entry.get()
    if id == "" or id==0:
        tmsg.showerror("Error", "please fill the entry")
        #return
    else:
        conn = sqlite3.connect('dress.db')
        c = conn.cursor()
        c.execute("DELETE FROM dress WHERE dress_id=?", (id,))
        conn.commit()
        tmsg.showinfo("REMOVE", " the dress removed !")
        conn.close()


def go_back():
    root.destroy()


root = Tk()


def Remove(root):
    # frame = Frame(root)
    root.title('Remove a dress')
    root.configure(bg="#ffeff2")  # Light pink background color
    root.geometry("500x500")

    # Add a label for Dress ID
    label = Label(root, text="Dress ID", bg="#fed3e6", relief="solid", font=("Papyrus 16 bold"))
    label.place(x=85, y=170)

    # Entry widget for dress ID
    e1 = IntVar()
    entry = Entry(root, width=21, font=("Arial", 12), textvariable=e1)
    entry.place(x=210, y=176)

    # Button to remove a dress
    button = Button(root, text="Remove", bg="#fed3e6", relief="solid",
                    command=lambda: remove_dress(e1.get()), font=("Papyrus 19 bold"))
    button.place(x=300, y=300)

    # Button to go back
    btn_back = Button(root, text="Back", bg="#fed3e6", relief="solid",
                      command=go_back, font=("Papyrus 17 bold"))
    btn_back.place(x=90, y=300)

    root.mainloop()


def call():
    Remove(root)


call()
