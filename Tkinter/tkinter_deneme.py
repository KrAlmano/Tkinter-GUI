import tkinter as tk
import random as rd

form = tk.Tk()
form.title('Deneme Uygulaması')
form.geometry('500x400+250+75')
liste = []

for i in range(5):
    while len(liste)!=5:
        a = rd.randint(0,50)
        if a not in liste:
            liste.append(a)



def göster():
    label.config(text=liste,bg='blue')


def saydamlaştır():
    form.wm_attributes('-alpha',0.3)


def düzelt():
    form.wm_attributes('-alpha',0.9)

def ekranBüyüt():
    form.state('zoomed')

def ekranKüçült():
    form.state('iconic')





label = tk.Label(form,fg='green',bg='white')
label.pack()

göster = tk.Button(form,text='Göster',fg='red',bg='white',command=göster)
göster.pack()


saydamlaştır = tk.Button(form,text='Saydamlaştır',fg='red',bg='white',command=saydamlaştır)
saydamlaştır.pack()



düzelt = tk.Button(form,text='Düzelt',fg='red',bg='white',command=düzelt)
düzelt.pack()



ekranBüyüt = tk.Button(form,text='EkranBüyüt',fg='red',bg='white',command=ekranBüyüt)
ekranBüyüt.pack()



ekranKüçült = tk.Button(form,text='EkranKüçült',fg='red',bg='white',command=ekranKüçült)
ekranKüçült.pack()



form.mainloop()