from tkinter import *
from PIL import Image, ImageTk
from buy_a_dress import show_dress_image
from Search_frame import show_dress_images

def client_options(root):
    def searchh(root):
        root.destroy()
        new_win = Tk()
        show_dress_images(new_win)
    def browse(root):
        root.destroy()
        new_win = Tk()
        show_dress_image(new_win)
    frame=Frame(root)
    padx=10
    pady=10
    font=("Papyrus 15 bold")
    #To convert format of image to png
    img= Image.open("client_options.png")
    #To resize image to make it bigger
    img=img.resize((550,350))
    img_tk=ImageTk.PhotoImage(img)
    Label(root, image=img_tk).place(x=0, y=0)
    def center_screen():
            w=550
            h=350
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
    btn_browse=Button(root,text="show all dresses",font=font,bg="black",fg="pink")#,command=open_login_admin)
    btn_browse.place(x=310,y=170)
    btn_browse.config(command=lambda: browse(root))
      #botton for Customer
    btn_search=Button(root,text="Seach",font=font,bg="black",fg="pink")
    btn_search.place(x=350,y=100)
    btn_search.config(command=lambda: searchh(root))
    #btn_customer.config(command=lambda: Customer_login.customer_login(root))
    root.title("Welcome")
    center_screen()
    resizable_screen()
    
    root.mainloop()

'''
def call():
    root = Tk()
    client_options(root)
    root.mainloop()
call()
'''