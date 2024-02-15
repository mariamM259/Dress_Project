from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import tkinter.messagebox as tmsg
from tkinter import ttk


root = Tk()




def add(root):
    # function back
    def back_b():
        root.destroy()

    # frame = Frame(root)

    def add_data():
        if entry1.get() == "" or entry2.get() == "" or entry3.get() == "" :
            tmsg.showerror("Error", "please fill all the entry")
            #return
        else:
            conn = sqlite3.connect('dress.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO dress  VALUES (NULL,?,?,?,0)", (entry1.get(), entry2.get(), entry3.get()))
            conn.commit()
            tmsg.showinfo("ADD","the dress added successfully!")
            conn.close()

    # Create the main window

    root.title('Add a dress')
    # Set the background color
    root.configure(bg="#ffeff2")  # Light pink background color

    root.geometry("500x500")

    # Add a label with any sentence
    label = Label(root, text="   Path  ", bg="#fed3e6", bd=1, relief="solid", font=("Papyrus 16 bold"))
    label.place(x=100, y=120)

    # Entry  for dress  ID
    entry1 = Entry(root, width=23, font=("Arial", 12))
    entry1.place(x=200, y=128)

    label = Label(root, text=" Color ", bg="#fed3e6", bd=1, relief="solid", font=("Papyrus 16 bold"))
    label.place(x=100, y=190)

    # Entry  for dress  color
    entry2 = Entry(root, width=23, font=("Arial", 12))
    entry2.place(x=200, y=198)

    label = Label(root, text="  Price  ", bg="#fed3e6", bd=1, relief="solid", font=("Papyrus 16 bold"))
    label.place(x=100, y=260)

    # Entry for dress  price
    entry3 = Entry(root, width=23, font=("Arial", 12))
    entry3.place(x=200, y=268)

    # Button to add a dress
    button = Button(root, text="Add", bg="#fed3e6", relief="solid",
                    command=add_data, font=("Papyrus 19 bold"))
    # Place the button
    button.place(x=311, y=380)

    # button to back
    btn_back = Button(root, text="Back", bg="#fed3e6", relief="solid",
                      command=back_b, font=("Papyrus 17 bold"))
    btn_back.place(x=100, y=380)

    # Run the GUIS
    root.mainloop()


# the function to add in data base


def call():
    add(root)
    root.mainloop()


call()
