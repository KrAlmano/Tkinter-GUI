from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("OOP Lecture")
        self.geometry("400x400+350+90")

        self.my_text = ctk.CTkTextbox(self,width=300,height=250)
        self.my_text.pack(pady=10)

        self.my_button =ctk.CTkButton(self,text="Clear Box",command=self.clear)
        self.my_button.pack()

    def clear(self):
        self.my_text.delete("0.0",END)

app = App()
app.mainloop()