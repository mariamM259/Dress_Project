from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from client_optionss import client_options
import sqlite3

def sign_up(root):
    
    padx=10
    pady=10
    font=("Papyrus 19 bold")
    img= Image.open("sign_customer1.jpeg")
    #To resize image to make it bigger
    img=img.resize((700,700))
    img_tk=ImageTk.PhotoImage(img)
    Label(root, image=img_tk).place(x=0, y=0)

    lbl_username=Label(root,text='Username',bg='pink',fg='black',font=font)
    lbl_password=Label(root,text='Password',bg='pink',fg='black',font=font)

    e1=StringVar()
    e2=StringVar()
            
    en1=Entry(root,font=font,textvariable=e1)
    en2=Entry(root,show='*',font=font,textvariable=e2)
    def signup():
            e1=str(en1.get())
            e2=str(en2.get())
            conn=sqlite3.connect('dress.db')   
            cur=conn.cursor()
            if e1=="" or e2=="":
                msg.showerror("error","Please enter valid username or password")
                
            else:
                
               #refer to the database(customer_data)
                cur.execute("INSERT INTO customer_data(user_name,password)VALUES(?,?)",(e1,e2,))
                conn.commit()
                msg.showinfo("Right INPUT", "Valid Username and Password")
                en1.set=""
                en2.set=""
                root.destroy()
                new_win = Tk()
                client_options(new_win)
            conn.close()  
            
            
            
    btn_login=Button(root,text='Sign Up',bg='pink',fg='black',font=font,relief='flat',command=signup)
                
           
    lbl_username.place(x=40,y=90)
    lbl_password.place(x=40,y=180)
    en1.place(x=200,y=90)
    en2.place(x=200,y=180)
    btn_login.place(x=250,y=250)


    def center_screen():
        w=700
        h=700
        screenwidth=root.winfo_screenwidth()
        screenheight=root.winfo_screenheight()
        x=int((screenwidth-w)/2)
        y=int((screenheight-h)/2)
        root.geometry(f'{w}x{h}+{x}+{y}')
    
        
        
    def resizable_screen():
        root.resizable(False,False)
    root.title("Customer_Sign_UP")

    center_screen()
    resizable_screen()

    root.mainloop()
'''
def call():
    root = Tk()
    
    sign_up(root)
    root.mainloop()
call()
'''
