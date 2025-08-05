import tkinter as tk

form = tk.Tk()
form.geometry('500x500+350+75')
form.config(bg='pink')

scroll = tk.Scrollbar()
scroll.pack(side=tk.RIGHT,fill=tk.Y)


listbox= tk.Listbox(form, yscrollcommand=scroll.set,bg='pink')


for i in range(500):
    listbox.insert('end','Deneme'+str(i))

listbox.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
scroll.config(command=listbox.yview)



form.mainloop()