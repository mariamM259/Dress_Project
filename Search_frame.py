from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
#from client_optionss import client_options
# Declare photo_images as a global variable


photo_images = []


def show_dress_images(root):
    photo_images=[]
    def message_box(title, message):
        messagebox.showinfo(title, message)
    def back():
       root.destroy()
       new_win = Tk()
       from client_optionss import client_options
       client_options(new_win)

    def show_result(data):
        # Use global photo_images
        global photo_images

        # Clear existing content in inner_frame
        for widget in inner_frame.winfo_children():
            widget.destroy()

        for i, (colors, photo_path, price, dress_id) in enumerate(data):
            frame2 = Frame(inner_frame, bg="#ffeff2", padx=30, pady=10)

            # Load and resize the image
            img = Image.open(photo_path)
            img = img.resize((200, 300))
            img_tk = ImageTk.PhotoImage(img)
            print(photo_path, img)
            photo_images.append(img_tk)

            # Use a reference to the image to prevent garbage collection
            label = Label(frame2, image=img_tk, bg="#ffeff2", highlightbackground="#ffa9cc", highlightthickness=3)
            label.image = img_tk  # Reference to the image
            label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

            # Button to buy
            button = Button(frame2, text="Buy", bg="#fed3e6", highlightbackground="#ffa9cc", relief="solid",
                            font=("Papyrus", 13, "bold"))
            button.config(command=lambda dress_cost=price, dress_id=dress_id: on_buy_click(dress_cost, dress_id))
            button.grid(row=1, column=0, pady=5)

            # Label for colors
            label1 = Label(frame2, text=colors, highlightbackground="black", bg="#fed3e6",
                           font=("Papyrus", 13, "bold"), highlightthickness=2)
            label1.grid(row=1, column=1, pady=5)

            # Label for price
            label2 = Label(frame2, text=str(price), bg="#fed3e6", font=("Papyrus", 13, "bold"),
                           highlightbackground="black", highlightthickness=2)
            label2.grid(row=1, column=2, pady=5)

            frame2.grid(row=(i // 4) + 2, column=i % 4)

        # Update the inner_frame to reflect changes
        inner_frame.update_idletasks()

    def get_data(colorss):
        conn = sqlite3.connect('dress.db')
        cursor = conn.cursor()

        # Query the database for dress information based on color
        cursor.execute("SELECT colors, dress_photo, price, dress_id FROM dress where colors = ?", (colorss,))
        data = cursor.fetchall()
        if data:
            show_result(data)
        else:
            message_box("No Data", "No dresses found with the selected color.")

        conn.close()
        return data

    def on_buy_click(dress_cost, dress_id):
        # Ask a question before proceeding
        response = messagebox.askquestion("Confirmation", f"Do you want to buy the Dress that costs: {dress_cost}?")
        if response == "yes":
            update_buying_number(dress_id)
            message_box("Purchase Confirmation", f"Successfully bought Dress that costs: {dress_cost}. "
                                                 "Come after a week from now to get your dress.")
        else:
            message_box("Purchase Canceled", "Purchase canceled.")

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

    def c1():
        # Triggered when the search button is clicked
        get_data(a_color.get())

    # Tkinter setup for the main window
    #root = Tk()
    root.title('SEARCH FOR  DRESS')
    root.configure(bg="red")

    frame = Frame(root, bg="#ffeff2")
    frame.pack(fill="both", expand=True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1200
    window_height = 700
    x_position = ((screen_width - window_width) // 2)
    y_position = ((screen_height - window_height) // 2) - 60
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    content_height = 50 // 4 * (600 + 60) + 30
    canvas = Canvas(frame, bg="#ffeff2", scrollregion=(0, 0, 0, content_height))
    canvas.pack(side="left", fill="both", expand=True)

    inner_frame = Frame(canvas, bg="#ffeff2")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    scrollbar = Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Search button and entry
#    col = Label(frame, text="color", bg="#fed3e6", highlightbackground="#ffa9cc"و
                   #        font=("Papyrus", 11, "bold"))
    #col.pack(side='top', pady=10, padx=10)
    search_button = Button(frame, text="search", bg="#fed3e6", highlightbackground="#ffa9cc", relief="solid",
                           font=("Papyrus", 11, "bold"), command=c1)
    a_color = StringVar()
    e3 = Entry(frame, textvariable=a_color, width=30, highlightbackground="#ffa9cc", highlightcolor="#ffa9cc")

    e3.pack(side='top', pady=10, padx=10)
    search_button.pack(side='top', pady=10, padx=10)
    back_button = Button(frame, text="back", bg="#fed3e6", highlightbackground="#ffa9cc", relief="solid",
                           font=("Papyrus", 11, "bold"),command=back)
    back_button.pack(side='top', pady=10, padx=10)
    # Start the Tkinter event loop
    root.mainloop()

# Call the function to show the dress images
#show_dress_image()
