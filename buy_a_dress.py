from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as msg
def message_box(title, message):
    messagebox.showinfo(title, message)

def show_dress_image(root):
    def on_buy_click(dress_cost, dress_id):
        # Ask a question before proceeding
        print("yess",dress_id)
        response=msg.askquestion("Confirmation", f"Do you want to buy the Dress that costs: {dress_cost}?")
        #response = messagebox.askquestion("Confirmation", f"Do you want to buy the Dress that costs: {dress_cost}?")
        if response == "yes":
            print("yes")
            #msg.message_box("Purchase Confirmation", f"Successfully bought Dress that costs: {dress_cost},Come after a week from now to get your dress.")
            update_buying_number(dress_id)
        else:
            #msg.message_box("Purchase Canceled", "Purchase canceled.")
            print("no")
    def update_buying_number(dress_id):
        conn = sqlite3.connect('dress.db')
        cursor = conn.cursor()

        # Fetch the current buying number
        cursor.execute("SELECT buyingNumber FROM dress WHERE dress_id = ?", (dress_id,))
        buying_number = cursor.fetchone()[0]

        # Update the buying number
        updated_buying_number = buying_number + 1
        cursor.execute("UPDATE dress SET buyingNumber = ? WHERE dress_id = ?", (updated_buying_number, dress_id))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    def back():
       root.destroy()
       new_win = Tk()
       from client_optionss import client_options
       client_options(new_win)
    # Create the main window
    #root = Tk()
    root.title('BUY A DRESS')

    # Set the background color
    root.configure(bg="#ffeff2")  # Light pink background color

    # Calculate the window position to center it on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1200
    window_height = 700
    x_position = ((screen_width - window_width) // 2)
    y_position = ((screen_height - window_height) // 2)-60

    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def get_data():
        conn = sqlite3.connect('dress.db')
        cursor = conn.cursor()

        # Fetch data from the database
        cursor.execute("SELECT colors, dress_photo, price,dress_id FROM dress ")
        data = cursor.fetchall()

        # Close the connection
        conn.close()

        return data

    # Create a frame to hold the images and buttons
    frame = Frame(root, bg="#ffeff2")  # Removed unnecessary padding
    frame.pack(fill="both", expand=True)

    # Number of times to duplicate the photo
    data = get_data()

    # Create a Canvas widget to hold the frames and allow scrolling
    content_height = len(data) // 4 * (600 + 60) +30 # Adjust with your frame height and padding
    canvas = Canvas(frame, bg="#ffeff2", scrollregion=(0, 0, 0, content_height))  # Adjust the scroll region as needed
    canvas.pack(side="left", fill="both", expand=True)

    # Create a frame inside the canvas to hold the images and buttons
    inner_frame = Frame(canvas, bg="#ffeff2")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # List to store PhotoImage objects
    photo_images = []

    for i, (colors, photo_path, price,dress_id) in enumerate(data):
        # Create a new frame to hold the label and button for each image
        frame2 = Frame(inner_frame, bg="#ffeff2", padx=30, pady=10)
        print(i, ' ', colors, " ", photo_path)
        img = Image.open(photo_path)
        img = img.resize((200, 300))  # Adjusted the size for better fit
        img_tk = ImageTk.PhotoImage(img)

        # Store the PhotoImage object in the list
        photo_images.append(img_tk)

        # Display the image in the frame with a thin border
        label = Label(frame2, image=img_tk, bg="#ffeff2", highlightbackground="#ffa9cc", highlightthickness=3)
        label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)  # Added some padding

        # Create a button with specified properties
        button = Button(frame2, text="Buy", bg="#fed3e6", highlightbackground="#ffa9cc", relief="solid", font=("Papyrus", 13, "bold"))
        button.config(command=lambda dress_cost=price, dress_id=dress_id: on_buy_click(dress_cost,dress_id))
        button.grid(row=1, column=0, pady=5)  # Adjusted row for buttons

        # Create a label with specified properties
        label1 = Label(frame2, text=colors, highlightbackground="black", bg="#fed3e6", font=("Papyrus", 13, "bold"), highlightthickness=2)
        label1.grid(row=1, column=1, pady=5)
        label2 = Label(frame2, text=str(price), bg="#fed3e6", font=("Papyrus", 13, "bold"), highlightbackground="black", highlightthickness=2)
        label2.grid(row=1, column=2, pady=5)

        # Pack the inner frame
        frame2.grid(row=i // 4, column=i % 4)

    # Add a vertical scrollbar
    scrollbar = Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create the "Back" button
    back_button = Button(inner_frame, text="Back", bg="#fed3e6", highlightbackground="#ffa9cc", relief="solid", font=("Papyrus", 20, "bold"),command=back)
    back_palce=int(len(data))//4+1
    print(back_palce)
   # back_button.grid(row=back_palce,column=0,padx=20,pady=50,columnspan=4)
    back_button.grid(row=back_palce, column=0, padx=20, pady=50, columnspan=4)
    
    # Run the GUI
    root.mainloop()

# Call the function to show the dress images
#show_dress_image()
'''
def call():
    root = Tk()
    show_dress_image(root)
    root.mainloop()
call()
'''