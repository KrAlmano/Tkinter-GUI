import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk


form = tk.Tk()
form.geometry('500x500+350+75')
form.title('Review')
form.config(bg='black')

lbl_isim = tk.Label(form,text='İsim',fg='white',bg='black',width=10,font='Times 15 italic').place(x=10,y=30)

x=tk.StringVar()

def yazdir():
    print(x.get())
    messagebox.showinfo(title='Message1',message='Check message!')

liste = ['A','B','C','D','E']
combo_isim = Combobox(form,values=liste,height=3,textvariable=x).place(x=170,y=30)


buton = ttk.Button(form,text='Yazdır',command=yazdir).pack()







form.mainloop()