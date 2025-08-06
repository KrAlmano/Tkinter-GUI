from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Switch")
root.geometry("300x300+400+90")

def switcher():
    my_label.configure(text=switch_var.get())

def click():
    my_switch.toggle()

switch_var = ctk.StringVar(value="on")

my_switch = ctk.CTkSwitch(root,text="Switch",command=switcher,
                          variable=switch_var,onvalue="on",offvalue="off")
my_switch.pack(pady=20)

my_label=ctk.CTkLabel(root,text="")
my_label.pack(pady=20)


my_button = ctk.CTkButton(root,text="Click",command=click)
my_button.pack(pady=10)







root.mainloop()