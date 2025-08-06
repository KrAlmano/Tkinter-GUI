from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")


root = ctk.CTk()
root.title("RadioButtons")
root.geometry("700x300+350+80")

my_label=ctk.CTkLabel(root,text="Do you like?")
my_label.pack(pady=10)

def submit():
    if rad_value.get()=="Other":
        my_label2.configure(text="Please make an selection")
    elif rad_value.get()=="Yes":
        my_label2.configure(text="Good Choice")
    else:
        my_label2.configure(text="Bad Choice")


rad_value=ctk.StringVar(value="Other")

my_rad1=ctk.CTkRadioButton(root,text="Yes",value="Yes",variable=rad_value,
                           radiobutton_height=20,
                           radiobutton_width=20,
                           corner_radius=2,
                           border_width_unchecked=2,
                           border_width_checked=2,
                           border_color="red",
                           hover_color="pink",fg_color="green")
my_rad1.pack(pady=10)


my_rad2=ctk.CTkRadioButton(root,text="No",value="No",variable=rad_value)
my_rad2.pack(pady=10)

my_button = ctk.CTkButton(root,text="Submit",command=submit)
my_button.pack(pady=10)

my_label2=ctk.CTkLabel(root,text="")
my_label2.pack(pady=10)


root.mainloop()