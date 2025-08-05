import tkinter as tk

form = tk.Tk()
form.title('Place')
form.geometry('500x500+350+75')

buton = tk.Button(text='Deneme',fg='red',bg='green',font='Times 17 bold')
buton.place(x=175,y=175)

#Dinamik olarak oynatmak için

buton2= tk.Button(text='Dinamik',fg='white',bg='black',font='Times 15')
buton2.place(relx=0.5,rely=0.5)


#Buton Büyüklüğü 

buton3 = tk.Button(text='Büyüklük',fg='green',bg='black',font='Times 12 bold')
buton3.place(width=120,height=100)


form.mainloop()