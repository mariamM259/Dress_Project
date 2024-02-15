from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
import sqlite3
#from buy_a_dress import show_dress_image
from sign_customer import sign_up
from client_optionss import client_options
def customer_Login(root):
    padx = 10
    pady = 10
    font = ("Papyrus 15 bold")
    img = Image.open("login_customer.jpeg")
    img = img.resize((700, 700))
    img_tk = ImageTk.PhotoImage(img)
    Label(root, image=img_tk).place(x=0, y=0)

    lbl_username = Label(root, text='Username', bg='pink', fg='black', font=font)
    lbl_password = Label(root, text='Password', bg='pink', fg='black', font=font)

    e1 = StringVar()
    e2 = StringVar()
    en1 = Entry(root, font=font, textvariable=e1)
    en2 = Entry(root, show='*', font=font, textvariable=e2)

    def login_customer():
        user = en1.get()
        password = en2.get()
        print(password)
        if user == "" or password == "":
            msg.showerror("Error", "Please enter a valid username or password")
            en1.set("")
            en2.set("")
        else:
            conn = sqlite3.connect('dress.db')
            cur = conn.cursor()
    
            cur.execute("SELECT id FROM Customer_data WHERE user_name =? AND password=?", (user, password))
            data = cur.fetchall()
            print(data)
            if len(data) > 0:  # Check if the length of data is greater than zero
                root.destroy()
                new_win = Tk()
                client_options(new_win)
            else:
                msg.showerror("Error", "Please enter a valid username or password")
                en1.set("")
                en2.set("")
    
            conn.close()

            conn.close()
    def signup_customer():
         root.destroy()
         new_win = Tk()
         sign_up(new_win)
                
    btn_login = Button(root, text='Login', bg='pink', fg='black', font=font, relief='flat', command=login_customer)
    btn_sign_up = Button(root, text='Sign Up', bg='pink', fg='black', font=font, relief='flat',command=signup_customer)

    lbl_username.place(x=240, y=100)
    lbl_password.place(x=240, y=200)
    en1.place(x=350, y=100)
    en2.place(x=350, y=200)
    btn_login.place(x=310, y=290)
    btn_sign_up.place(x=450, y=290)

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

    root.title("Customer_Login")

    center_screen()
    resizable_screen()
    root.mainloop()

'''
def call():
    root = Tk()
    customer_Login(root)
    root.mainloop()


call()
'''