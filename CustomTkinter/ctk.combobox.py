from tkinter import*
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

root.title("Combobox GUI")
root.geometry("500x500+550+100")

#For combobox
def color_picker(choice):
    output_label.configure(text=choice, text_color=choice)

#For button
def color_picker2():
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())

def color_picker_yellow():
    my_combo.set("Yellow")
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())
    #OR
    #output_label.configure(text="Yellow", text_color="yellow")

my_label = ctk.CTkLabel(root,text="Pick a color",font=("helvenica",19))
my_label.pack(pady=20)


colors = ["Red","Green","Blue"]

my_combo = ctk.CTkComboBox(root,values=colors,
                           height=50,
                           width=200,font=("helvetica",30),
                           dropdown_font=("helvetica",20),
                           corner_radius=30,
                           border_width=5,
                           border_color="red",
                           button_color="red",
                           button_hover_color="green",
                           dropdown_hover_color="white",
                           dropdown_fg_color="black",
                           dropdown_text_color="orange",
                           text_color="silver",
                           justify="center",
                           state="normal")  #içini "disabled yaparsak çalışmayacaktır"
my_combo.pack(pady=10)


my_button= ctk.CTkButton(root,text="Pick",command=color_picker2)
my_button.pack(pady=10)

#Yellow Button
yellow_button = ctk.CTkButton(root,text="Pick Yellow",command=color_picker_yellow)
yellow_button.pack(pady=10)


output_label= ctk.CTkLabel(root,text="",font=("Helvetica",30))
output_label.pack(pady=20)



root.mainloop()