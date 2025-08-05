import tkinter as tk
import time 

form = tk.Tk()
form.title('Clock App')
form.geometry('500x500+350+75')
form.config(bg='yellow')

def gettime():
    time_format= time.strftime('%H:%M:%S')
    time_label.config(text=time_format)
    time_label.after(200,gettime)   #MS , Ping




time_label=tk.Label(bg='white',font='Times 35 bold')
time_label.place(x=160,y=190)

gettime()


baslık = tk.Label(text='Digital Clock App',font='Times 15 bold',bg='yellow').pack()




form.mainloop()