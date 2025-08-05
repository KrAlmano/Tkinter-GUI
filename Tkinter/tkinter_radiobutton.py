import tkinter as tk


form = tk.Tk()
form.geometry('500x500+350+75')

def kontrol():
    if x.get()=='1':
        print(f'buton1')
    elif x.get()=='2':
        print(f'buton2')
    else:
        print(f'buton2 and buton1')

buton = tk.Button(form,text='Tıkla',fg='black',bg='white',activebackground='green',command=kontrol)
buton.pack()


x = tk.StringVar()


radio= tk.Radiobutton(form,text='Radio Button1',activebackground='red',value=1,variable=x)
radio.pack()

radio2= tk.Radiobutton(form,text='Radio Button2',activebackground='green',value=2,variable=x)
radio2.pack()


form.mainloop()