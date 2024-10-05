import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def change_window_content():
    frame.destroy()
    button_frame.destroy()

    # Create and display new content
    new_content = tk.Label(window, text="Choose your preferred Sign Language",
                           font=("Georgia", 16), bg="white", fg="#00467F")
    new_content.pack(pady=40)

    #Create a button for American Sign Language
    as_button = tk.Button(window, text="American Sign Language", command=run_other_script, font=("Georgia", 18),
    bg="#00467F", fg="white",width=20,borderwidth=0)
    as_button.place(relx=0.5, rely=0.35, anchor='center',height=35)
    #Create a button for Indian Sign Language
    is_button = tk.Button(window, text="Indian Sign Language", command=run_script, font=("Georgia", 17),
    bg="#00467F", fg="white", width = 20,borderwidth=0)
    is_button.place(relx=0.5, rely=0.50, anchor='center',height=35)
    #Close Button
    close_button = tk.Button(window, text="Exit", command=window.destroy, font=("Georgia", 16), bg="#00467F",
                             fg="white", width=10, borderwidth=0)
    close_button.place(relx = 0.5,rely= 0.80,anchor ='center')
def run_script():
    with open("C:/Users/joelb/PycharmProjects/pythonProject1/ISL_testing.py", "r") as file:
        exec(file.read())

def run_other_script():
    with open("C:/Users/joelb/PycharmProjects/pythonProject1/ASL_testing.py", "r") as file:
        exec(file.read())

def create_window():
    global window,frame,button_frame
    #Create the main window
    window = tk.Tk()
    window.title("SignSpeak")
    window.geometry("600x400")
    #window.resizable(False,False)
    window.configure(bg='white')

    # Logo
    logo = ImageTk.PhotoImage(file="C:/Users/joelb/Sign/sign1.png")
    window.iconphoto(False, logo)

    #Creating a frame to hold the image and text
    frame = tk.Frame(window,bg='white')
    frame.place(relx=.5,rely=.35,anchor='center')

    #Loading image
    image = Image.open("C:/Users/joelb/Sign/sign.png")
    image = image.resize((200,150))
    img =ImageTk.PhotoImage(image)

    #Creating a label for the image
    image_label = tk.Label(frame,image = img,bg='white')
    image_label.image = img
    image_label.pack(side="top",padx = (10,10),pady=(20,0))


    #Creating a label for the text
    text_label = tk.Label(frame,text = " SignSpeak",font = ("Georgia",27),fg = "#00467F",bg="white")
    text_label.pack(side="top",padx=(0,5),pady=(2,0))

    #Another label
    text2_label = tk.Label(frame,text = "Bridge the Gap",font = ("Georgia",14),fg = "#00467F",bg="white")
    text2_label.pack(side="top",padx=(0,5),pady=(0,0))

    # Frame to hold both the buttons
    button_frame = tk.Frame(window, bg='white')
    button_frame.place(relx=.5, rely=.80, anchor='center')

    # Button that will trigger the change
    change_button = tk.Button(button_frame, text= "Explore", command= change_window_content,font=("Georgia",16),bg="#00467F", fg = "white", width = 10,borderwidth=0)
    change_button.pack(side ="left",padx=20,pady=(0,0))
    close_button = tk.Button(button_frame, text="Exit", command=window.destroy,font=("Georgia",16),bg="#00467F", fg = "white", width = 10,borderwidth=0)
    close_button.pack(side ="right",padx=20,pady=(0,0))


    #Starting Tkinter event loop
    window.mainloop()

create_window()