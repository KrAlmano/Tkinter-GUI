from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Textbox Editor")
root.geometry("400x200+400+90")

is_font_changed = False

def change():
    global is_font_changed
    if is_font_changed==False:
     my_font.configure(underline=False,overstrike=True)
     is_font_changed = True
    else:
       my_font.configure(underline=True,overstrike=False)
       is_font_changed = False
       

my_font = ctk.CTkFont(family="Helvetica",size=34,
                      weight="bold",
                      slant="italic",
                      underline=True,
                      overstrike=False) 


my_label = ctk.CTkLabel(root,text="Deneme Yazısı",font=my_font)
my_label.pack(pady=20)


my_button = ctk.CTkButton(root,text="Change Font",command=change)
my_button.pack(pady=20)




root.mainloop()