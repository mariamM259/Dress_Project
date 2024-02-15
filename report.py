from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()


def Report(root):

    def back_b():
        root.destroy()

    frame = Frame(root)
    # Create the main window

    root.title('Report')
    # Set the background color
    root.configure(bg="#ffeff2")  # Light pink background color

    root.geometry("500x500")
    # label for report
    label = Label(root, text="  Report  ", bg="#fed3e6", bd=1, relief="solid", font=("Papyrus 16 bold"))
    label.place(x=200, y=0)
    # button back
    btn_back = Button(root, text="Back", bg="#fed3e6", relief="solid",
                      command=back_b, font=("Papyrus 15 bold"))
    btn_back.place(x=40, y=420)
    # button ok
    btn_back = Button(root, text="OK", bg="#fed3e6", relief="solid",
                      command=back_b, font=("Papyrus 15 bold"))
    btn_back.place(x=400, y=420)

    #############################
    def create_tree(plc, lists):
        tree = ttk.Treeview(plc, height=13, column=(lists), show='headings')
        n = 0
        while n is not len(lists):
            tree.heading("#" + str(n + 1), text=lists[n])
            tree.column("" + lists[n], width=90)
            n = n + 1
        return tree
    def fetch():
        conn = sqlite3.connect('dress.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM dress")
        rows = cur.fetchall()
        return rows

    def all_book():
        f1 = Frame(root, bg="black", height=340, width=475)
        f1.place(x=12, y=50)
        lists = ('id','path','color','price','buying_no')
        trees = (create_tree(f1, lists))
        trees.delete(*trees.get_children())
        for row in fetch():
            trees.insert("", END, values=row)
        trees.place(x=15, y=22)
        # btn_back = Button(f1, text="Back", fg="black", bg="purple",
        #                   font='Papyrus 10 bold', width=10)
        # btn_back.place(x=250, y=400)
    all_book()
    ######################################

    frame.place(anchor='center', relx=0.5, rely=0.5)
    # Run the GUI
    root.mainloop()


# Call the function to create the GUI

def call():
    Report(root)
    root.mainloop()


call()