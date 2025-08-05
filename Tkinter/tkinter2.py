#İnput Dersleri

import tkinter as tk


form = tk.Tk()

form.title('Entry Dersi')
form.geometry('500x450+350+75')


giris = tk.Entry(fg='black', bg='white')
giris.pack(side=tk.LEFT)
giris2=tk.Entry(fg='black',bg='white')
giris2.pack(side=tk.RIGHT)

form.mainloop()