from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("500x500+350+75")


my_button = customtkinter.CTkButton(root,text="Almano")
my_button.pack(pady=220)



root.mainloop()