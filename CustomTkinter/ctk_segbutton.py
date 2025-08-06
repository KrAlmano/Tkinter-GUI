from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Segmented Button")
root.geometry("400x400+400+100")

def clicker(value):
    my_label.configure(text=f'Hello! {value}')

my_values = ["A","B","C"]
my_seg_button = ctk.CTkSegmentedButton(root,values=my_values,command=clicker,
                                       width=300,height=100,
                                       font=("Helvetica",18),
                                       corner_radius=30,
                                       border_width=5,
                                       selected_color="green",
                                       fg_color="white",
                                       selected_hover_color="pink",
                                       unselected_color="red",
                                       unselected_hover_color="orange",
                                       text_color="black",
                                       state="normal",#or disabled
                                       text_color_disabled="blue")
my_seg_button.pack(pady=20)


my_label = ctk.CTkLabel(root,text="",font=("Helvetica",18))
my_label.pack(pady=10)

root.mainloop()