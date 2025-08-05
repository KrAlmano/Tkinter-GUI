from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


root = customtkinter.CTk()


root.title("CTK Button")
root.geometry("500x500+350+75")


def hello():
    my_label.configure(text=my_button.cget("text"))

my_button = customtkinter.CTkButton(root,
                                    text="Almano",
                                    command= hello,
                                    height=100,
                                    width=200,
                                    font=("Helvetica",14),
                                    text_color="#3C0676",
                                    fg_color="red",
                                    hover_color="blue",
                                    corner_radius=30,
                                    bg_color="white",
                                    border_width=10,
                                    border_color="yellow",
                                    state="normal")
                                        
my_button.pack(pady=80)

my_label = customtkinter.CTkLabel(root,text="")
my_label.pack(pady=20)






root.mainloop()