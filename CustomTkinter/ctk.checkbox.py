from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")


root = ctk.CTk()

root.title("CheckBox")
root.geometry("500x500+350+75")

def game():
    if check_var.get()=="on":
        my_label.configure(text= "You clicked the button")
        text_var.set("Awesome!")
    else:
        my_label.configure(text= "You didn't click the button")
    
    
def clear():
    my_check.deselect()
    text_var.set("Would you like to play game?")
   



    
#Checkbox State
check_var = ctk.StringVar(value="off")
#Checkbox text
text_var = ctk.StringVar(value="Would you like the play a game")
my_check = ctk.CTkCheckBox(root,text="Would you like the play a game",
                           variable=check_var,
                           onvalue="on",offvalue="off",
                           checkbox_height=40,
                           checkbox_width=40,
                           font=("helvetica",18),
                           corner_radius=40,
                           fg_color="yellow",
                           hover_color="green",
                           text_color="red",
                           hover=False,
                           textvariable=text_var,
                           )
my_check.pack(pady=40)


my_button = ctk.CTkButton(root,text="Submit",command=game)
my_button.pack(pady=10)

clear_button = ctk.CTkButton(root,text="Clear",command=clear)
clear_button.pack(pady=10)

toggle_button = ctk.CTkButton(root,text="Toggle",command=my_check.toggle)
toggle_button.pack(pady=10)


my_label = ctk.CTkLabel(root,text="")
my_label.pack(pady=20)



root.mainloop()