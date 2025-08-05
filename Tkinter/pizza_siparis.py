import tkinter as tk

form = tk.Tk()
form.geometry('500x500+350+75')
form.title('Pizza Sipariş Programı')

baslik = tk.Label(text='Pizza Sipariş Uygulamasına Hoşgeldin',fg='green',bg='white',font='Times 16 bold').pack()


lb_ad = tk.Label(form,text='Ad-Soyad',bg='pink',font='Times 12 italic').place(x=10,y=40)
lb_boyut = tk.Label(form,text='Boyut',bg='pink',font='Times 12 italic').place(x=10,y=70)
lb_icindekiler = tk.Label(form,text='İçindekiler',bg='pink',font='Times 12 italic').place(x=10,y=100)
lb_adres = tk.Label(form,text='Adres',bg='pink',font='Times 12 italic').place(x=10,y=130)


entry = tk.StringVar()
entry1= tk.StringVar()

entry_ad = tk.Entry(textvariable=entry).place(x=90,y= 45)
entry_adress = tk.Entry(textvariable=entry1).place(x=90,y= 135)

boyut = tk.StringVar()
boyut.set(' ') #Başlangıç Değerlerini Sıfırlar

radbuton_kucuk= tk.Radiobutton(form,text='Küçük Boy',activebackground='green',value='Küçük Boy',variable=boyut).place(x=90 , y=75)
radbuton_orta= tk.Radiobutton(form,text='Orta Boy',activebackground='green',value='Orta Boy',variable=boyut).place(x=170 , y=75)
radbuton_buyuk= tk.Radiobutton(form,text='Büyük Boy',activebackground='green',value='Büyük Boy',variable=boyut).place(x=240 , y=75)


deger1 = tk.StringVar()
deger2 = tk.StringVar()
deger3 = tk.StringVar()


check1 = tk.Checkbutton(form,text='Sucuklu',activebackground='green',variable=deger1,onvalue='Sucuklu',offvalue='').place(x=90,y=100)
check2 = tk.Checkbutton(form,text='Zeytinli',activebackground='green',variable=deger2,onvalue='Zeytinli',offvalue='').place(x=160,y=100)
check3 = tk.Checkbutton(form,text='Mısır',activebackground='green',variable=deger3,onvalue='Mısır',offvalue='').place(x=230,y=100)

def siparis_ver():
    label_bilgi = tk.Label(form,text='Sipariş Bilgileri',bg='white',fg='black',font='Times 14 bold').place(x=170,y=220)
    lb_ad = tk.Label(form,text='Ad-Soyad',bg='pink',font='Times 12 italic').place(x=10,y=260)
    lb_boyut = tk.Label(form,text='Boyut',bg='pink',font='Times 12 italic').place(x=10,y=290)
    lb_icindekiler = tk.Label(form,text='İçindekiler',bg='pink',font='Times 12 italic').place(x=10,y=320)
    lb_adres = tk.Label(form,text='Adres',bg='pink',font='Times 12 italic').place(x=10,y=350)   

    lb_ad1 = tk.Label(form,text=entry.get(),font='Times 12 italic').place(x=100,y=260)
    lb_boyut1 = tk.Label(form,text=boyut.get(),font='Times 12 italic').place(x=100,y=290)
    lb_icindekiler1 = tk.Label(form,text=deger1.get() + ' ' + deger2.get()+' '+deger3.get(),font='Times 12 italic').place(x=100,y=320)
    lb_adres1 = tk.Label(form,text=entry1.get(),font='Times 12 italic').place(x=100,y=350)  

def iptal_et():
    form.quit()

siparis= tk.Button(form,text='Sipariş Ver',activebackground='green', command=siparis_ver).place(x=110, y=160)


iptal= tk.Button(form,text='İptal Et',activebackground='red', command=iptal_et).place(x=200, y=160)



form.mainloop()
