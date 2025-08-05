import tkinter as tk

form = tk.Tk()
form.geometry('500x500+350+75')


x=tk.IntVar()
x.set(0)

def kontrol():
    if x.get()==0:
        print('Onaylanmadı')
    else:
        print('Onaylandı')

check = tk.Checkbutton(form,text='Onay',fg='black',bg='white',variable=x,command=kontrol)
check.pack()




form.mainloop()