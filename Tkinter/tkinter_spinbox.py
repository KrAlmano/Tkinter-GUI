import tkinter as tk

form = tk.Tk()
form.geometry('500x500+350+75')

form.title('Spinbox')


form.config(bg='pink')
x=tk.IntVar()
spin = tk.Spinbox(form,from_=10,to=100,textvariable=x).pack()
y=tk.IntVar()
spin2= tk.Spinbox(form,from_=10,to=20,textvariable=y).pack()

def verial():
    print(x.get())
    print(y.get())

buton = tk.Button(form,text='VeriAl',command=verial).pack()


form.mainloop()