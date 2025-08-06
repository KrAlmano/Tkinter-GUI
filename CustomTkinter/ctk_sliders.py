from tkinter import*
import customtkinter as ctk

ctk.set_appearance_mode("dark")


root = ctk.CTk()
root.title("Sliders")
root.geometry("400x300+300+100")

def slide(value):
    my_label.configure(text=f'% {int(my_slide.get())}')

my_slide = ctk.CTkSlider(root,
                         from_=0,
                         to=100,
                         command=slide,
                         orientation="horizontal",
                         number_of_steps=20,
                         width=200,
                         height=50,
                         fg_color="white")
my_slide.pack(pady=20)

my_label = ctk.CTkLabel(root,text="")
my_label.pack(pady=20)

root.mainloop()