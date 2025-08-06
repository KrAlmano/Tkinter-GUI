from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Textbox Editor")
root.geometry("400x200+400+90")


def new():
    new_window = ctk.CTkToplevel(root,fg_color="silver")
    new_window.title("New window")
    new_window.geometry("300x300")
    new_window.resizable(False,True) #Widdth , Height


    def close():
        new_window.destroy()
        new_window.update()

    #Close the window

    new_button = ctk.CTkButton(new_window,text="Close the window",command=close)
    new_button.pack(pady=20)



my_button= ctk.CTkButton(root,text="Open New Window",command=new)
my_button.pack(pady=40)

root.mainloop()