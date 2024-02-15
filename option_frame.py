from tkinter import *
#from login_admin import *
from PIL import Image, ImageTk
import login_admin
#import Customer_login
from Customer_login import customer_Login
def adminLog(root):
    root.destroy()
    new_win = Tk()
    login_admin.login_admin(new_win)
def customerLog(root):
    root.destroy()
    new_win = Tk()
    customer_Login(new_win)
def login_options(root):
    frame=Frame(root)
    padx=10
    pady=10
    font=("Papyrus 22 bold")
    #To convert format of image to png
    img= Image.open("choose_frame.jpeg")
    #To resize image to make it bigger
    img=img.resize((700,700))
    img_tk=ImageTk.PhotoImage(img)
    Label(root, image=img_tk).place(x=0, y=0)
    def center_screen():
            w=700
            h=750
            screenwidth=root.winfo_screenwidth()
            screenheight=root.winfo_screenheight()
            x=int((screenwidth-w)/2)
            y=int((screenheight-h)/2)
            root.geometry(f'{w}x{h}+{x}+{y}')
            
    def resizable_screen():
            root.resizable(False,False) 

    '''def open_login_admin():
        frame.pack_forget()  # Hide the options frame
        log(root)  # Show the login_admin frame'''
    

        #botton for Admin 
    btn_admin=Button(root,text="Admin",font=font,bg="black",fg="pink")#,command=open_login_admin)
    btn_admin.place(x=500,y=450)
    btn_admin.config(command=lambda: adminLog(root))
      #botton for Customer
    btn_customer=Button(root,text="Customer",font=font,bg="black",fg="pink")
    btn_customer.place(x=500,y=550)
    btn_customer.config(command=lambda: customerLog(root))
    #btn_customer.config(command=lambda: Customer_login.customer_login(root))
    root.title("Welcome")
    center_screen()
    resizable_screen()
    
    root.mainloop()
def call():
    root = Tk()
    login_options(root)
    root.mainloop()
call()

#########################################################
'''
محتاجة اعمل ايه
1.login admin button اسم الفريمة بس
2.customer sign up doneeeeeeeeeeee 
3.customer login done
4.delete
5.add
6.generate bills
7.dfd بعد ما اخلص لرقم 3
8.search back done
9.browse back done


'''




