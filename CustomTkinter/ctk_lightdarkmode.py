from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_widget_scaling(1.5) #Scale widgets
ctk.set_window_scaling(1) #Scale Windows

root = ctk.CTk()
root.title("Textbox Editor")
root.geometry("400x400+400+90")

mode = "dark"

def change_mode():
    global mode
    if mode == "dark":
        ctk.set_appearance_mode("light")
        mode = "light"
    else:
        ctk.set_appearance_mode("dark")
        mode = "dark"

my_text= ctk.CTkTextbox(root,width=300,height=250)
my_text.pack(pady=20)

my_button = ctk.CTkButton(root,text="Change Mode",command=change_mode)
my_button.pack(pady=20)


root.mainloop()
