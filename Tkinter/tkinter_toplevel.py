import tkinter as tk

form = tk.Tk()
form.geometry('500x500+350+75')
form.title('Toplevel')


toplevel= tk.Toplevel(bg='pink')
toplevel.title('Toplevel2')
toplevel.geometry('240x240')

form.mainloop()
toplevel.mainloop()