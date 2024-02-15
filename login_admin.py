from tkinter import *
from tkinter import messagebox as msg
import sqlite3
from PIL import Image, ImageTk
from select1 import selectt  # Import the second frame module

def login_admin(root):
    root.title('Admin Login')
    root.configure(bg="#ffeff2")  # Light pink background color
    root.geometry("600x600")
    padx=10
    pady=10
    font=("Papyrus 21 bold")
    img= Image.open("login_admin.jpeg")
    #To resize image to make it bigger
    img=img.resize((700,700))
    img_tk=ImageTk.PhotoImage(img)
    Label(root, image=img_tk).place(x=0, y=0)


    def Admin_login(user, password):
        if user == "" or password == "":
            msg.showerror("Error", "Please enter valid username or password")
        else:
            conn = sqlite3.connect('dress.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM Admin WHERE user_name = ? AND password = ?", (user, password))
            res = cur.fetchone()
            if res is not None:
                msg.showinfo("Correct", "Valid username and password")
                root.destroy()
                new_win = Tk()
                selectt(new_win)  # Call the function to show the second frame
            else:
                msg.showerror("Error", "Please enter valid username or password")

    e1 = StringVar()
    e2 = StringVar()

    en1 = Entry(root, font=("Papyrus 21 bold"), textvariable=e1)
    en2 = Entry(root, show='*', font=("Papyrus 21 bold"), textvariable=e2)
    lbl_username = Label(root, text='Username', bg='pink', fg='black', font=("Papyrus 21 bold"))
    lbl_password = Label(root, text='Password', bg='pink', fg='black', font=("Papyrus 21 bold"))
    btn_login = Button(root, text='Login', bg='pink', fg='black', font=("Papyrus 21 bold"), relief='flat')
    btn_login.config(command=lambda: Admin_login(e1.get(), e2.get()))

    lbl_username.place(x=40, y=100)
    lbl_password.place(x=40, y=200)
    en1.place(x=200, y=100)
    en2.place(x=200, y=200)
    btn_login.place(x=240, y=290)

    def center_screen():
        w = 600
        h = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        x = int((screenwidth - w) / 2)
        y = int((screenheight - h) / 2)
        root.geometry(f'{w}x{h}+{x}+{y}')

    def resizable_screen():
        root.resizable(False, False)

    center_screen()
    resizable_screen()
    root.mainloop()
'''
def call():
    root = Tk()
    login_admin(root)
    root.mainloop()

call()
'''