import tkinter as tk
from tkinter import messagebox



form = tk.Tk()
form.geometry('500x500+350+75')
form.title('MessageBox')

def message():
    messagebox.showinfo(title='Message1',message='Check message!')
    messagebox.askretrycancel(title='Message2',message='Check Again !!!')
    messagebox.askyesno(title='Message3',message='Enough')
    messagebox.askquestion(title='Message4',message='Last Message')


buton = tk.Button(form,text='Mesaj Gelsin',fg='red', bg='white',command=message).pack()



form.mainloop()