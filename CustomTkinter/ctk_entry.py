from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("CTK Entry")
root.geometry("500x500+350+75")

def submit(): 
    if my_entry.get():
        my_label.configure(text=f'Hello {my_entry.get()}')

my_label = customtkinter.CTkLabel(root,text="",font=("Helvetica",24))
my_label.pack(pady=75)


my_entry = customtkinter.CTkEntry(root,placeholder_text="Enter your name",
                                  )

my_entry.pack(pady=10)


my_button = customtkinter.CTkButton(root,text="Submit",command=submit)
my_button.pack(pady=20)


root.mainloop()