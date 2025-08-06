from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Textbox Editor")
root.geometry("400x300+400+90")

def pick_color():
    my_label.configure(text=my_option.get(),text_color=my_option.get())



colors = ["Red","Blue","Green"]

my_option = ctk.CTkOptionMenu(root,values=colors)
my_option.pack(pady=20)


my_label = ctk.CTkLabel(root,text="",font=("Helvetica",24))
my_label.pack(pady=20)

pick_button = ctk.CTkButton(root,text="Pick Color",command=pick_color)
pick_button.pack(pady=20)

root.mainloop()
