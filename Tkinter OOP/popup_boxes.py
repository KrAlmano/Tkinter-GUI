from tkinter import *
from tkinter import messagebox,ttk


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("POPUP BOXES")
        photo = PhotoImage(file="deneme.png")
        self.iconphoto(False,photo)
        self.geometry("500x500+350+75")

        #Create Widgets
        self.my_label= Label(self,text="Enter Your Name :",font="Helvetica 20")
        self.my_label.pack(pady=20)

        self.my_entry = Entry(self,width=20,font="Helvetica 14")
        self.my_entry.pack(pady=20)

        self.my_button = ttk.Button(self,text="Pop-up",command=self.popup)
        self.my_button.pack(pady=20)


    def popup(self):
        if self.my_entry.get():
            messagebox.showinfo("Hello ", f"Hello {self.my_entry.get()}")   
        else:
            messagebox.showerror("Error","You suppose to enter your name ")


        



app = App()
app.mainloop()