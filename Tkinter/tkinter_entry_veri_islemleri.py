import tkinter as  tk 

form = tk.Tk()
form.title('Entry')
form.geometry('500x500+350+75')

entry = tk.Entry()
entry.pack()

entry2 = tk.Entry(show='*')
entry2.pack()


def veriAl():
    etiket['text'] = entry.get()

def veriSil():
    entry.delete(0,'end')
    entry2.delete(0,'end')





buton = tk.Button(text='Verileri al', fg='red',bg='white',command=veriAl)
buton.pack()

buton1 = tk.Button(text='Verileri sil', fg='red',bg='white',command=veriSil)
buton1.pack()

etiket = tk.Label(text='Verilerin buraya getirilmesi lazım')
etiket.pack()

form.mainloop()