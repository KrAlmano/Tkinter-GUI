import tkinter as tk

form = tk.Tk()
form.geometry('500x500+350+75')

label = tk.Label(text='Geometrik Yöneticiler')
label.pack(side=tk.TOP)

buton = tk.Button(text='Pack()',bg='red')
buton.pack(side=tk.BOTTOM,expand=tk.NO)

buton2=tk.Button(text='Unpack()',bg='green')
buton2.pack(padx=160,pady=120,ipadx=50,ipady=50)





form.mainloop()