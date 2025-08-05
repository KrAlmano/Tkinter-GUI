import tkinter as tk
sayac = 0

form = tk.Tk()
form.title('Sayac Uygulaması')
form.geometry('500x500+350+75')
form.config(bg='yellow')


x = tk.IntVar()
giris = tk.Entry(form,textvariable=x)
giris.place(x=90, y=60)
giris_label= tk.Label(text='Giris',bg='yellow',font='consoles 11 bold')
giris_label.place(x=10,y=58)

def geriSay():
    global sayac
    if sayac>=0 :
        sayım_label.config(text=sayac)
        sayac=sayac-1
        sayım_label.after(200,geriSay)

def ileriSay():
     global sayac
     if sayac>=0 :
        sayım_label.config(text=sayac)
        sayac=sayac+1
        sayım_label.after(200,ileriSay)

def cevir():
    global sayac
    sayac = sayac + int(x.get())
    return sayac


buton1 = tk.Button(form,text='Geri Say', activebackground='red',command=geriSay)
buton1.place(x=60,y=90)

buton2 = tk.Button(form,text='İleri Say', activebackground='red',command=ileriSay)
buton2.place(x=130,y=90)

buton3 = tk.Button(form,text='Cevir', activebackground='red',command=cevir)
buton3.place(x=200,y=90)

sayım_label= tk.Label(bg='white',font='Times 40 bold')
sayım_label.place(x=150,y=200)




form.mainloop()