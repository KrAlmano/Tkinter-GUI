import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox

form = tk.Tk()
form.geometry('500x500+350+75')

x=tk.StringVar()

python = ['Numpy','Pandas','Seaborn','Tkinter']


kutu = Combobox(form,values=python,height=3,textvariable=x).pack()

def yazdır():
    print(x.get())

buton = ttk.Button(form,text='Yazdır',command=yazdır).pack()



form.mainloop()