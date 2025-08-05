from tkinter import *
from tkinter import ttk
import sys


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Lesson")
        photo = PhotoImage(file='deneme.png')
        self.iconphoto(False, photo)
        self.geometry("500x500+350+75")

        #Create Status Variable
        self.status = True


        #Create widgets

        self.my_label= Label(self,text="Tkinter OOP",font="Helvatica 34", bg='yellow')
        self.my_label.pack(pady=20)

        self.my_button = ttk.Button(self,text="Change Text",command=self.change)
        self.my_button.pack(pady=20)

        My_frame(self)

    def change(self):
        if self.status == True:
            self.my_label.config(text="Tkinter OOP 2",bg='red')
            self.status = False
        else:
            self.my_label.config(text="Tkinter OOP",bg='yellow')
            self.status = True

class My_frame(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.my_button1 = ttk.Button(self,text="Change1",command=parent.change)
        self.my_button2 = ttk.Button(self,text="Change2",command=parent.change)
        self.my_button3 = ttk.Button(self,text="Change3",command=parent.change)

        self.my_button1.grid(row=0,column=0,padx=10)
        self.my_button2.grid(row=0,column=1,padx=10)
        self.my_button3.grid(row=0,column=2,padx=10)


app = App()
app.mainloop()

