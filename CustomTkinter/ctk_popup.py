from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Textbox Editor")
root.geometry("400x200+400+90")

def input_name():
    dialog = ctk.CTkInputDialog(text="What is your name",title="Hello there!",
                                fg_color="silver",
                                button_fg_color="red",
                                button_hover_color="pink",
                                button_text_color="black",
                                entry_fg_color="green",
                                entry_border_color="red",
                                entry_text_color="black")
    thing = dialog.get_input()
    if thing:
        my_label.configure(text=f"Hello {thing}")
    else:
        my_label.configure(text=f"Please enter your name")


my_button = ctk.CTkButton(root,text="Click",command=input_name)
my_button.pack(pady=20)


my_label = ctk.CTkLabel(root,text="")
my_label.pack(pady=10)


root.mainloop()