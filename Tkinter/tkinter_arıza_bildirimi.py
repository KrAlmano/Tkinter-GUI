import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk

form = tk.Tk()
form.geometry('300x300+350+75')
form.config(bg='black')
form.title('Arıza Bildirim Uygulaması')
lbl_baslik = tk.Label(form,text='Arıza Bildirim Uygulaması',bg='black',fg='white',font='Times 16 italic').pack()

lbl_ad = tk.Label(form,text='Kullanıcı Adı:',bg='black',fg='white',font='Times 12 italic')
lbl_ad.place(x=10,y=80)

lbl_sifre = tk.Label(form,text='Şifre:',bg='black',fg='white',font='Times 12 italic')
lbl_sifre.place(x=10,y=120)



entry_ad = tk.Entry(form)
entry_sifre = tk.Entry(form,show='*')

entry_ad.place(x=110,y=80)
entry_sifre.place(x=110,y=120)


def giris():
    if entry_ad.get() =='almano' and entry_sifre.get()=='12345':
        msg=messagebox.showinfo('Tebirkler',message='Giriş Başarılı')
        if msg=='ok':
            basvuru_form=tk.Toplevel()
            basvuru_form.geometry('300x300')
            basvuru_form.title('Arıza Bildirim Formu')
            basvuru_form.config(bg='yellow')
            baslık_label=tk.Label(basvuru_form,text='Arıza Bildirim Formu',bg='yellow',fg='black',font='Times 16 bold')
            baslık_label.pack()

            label_ad=tk.Label(basvuru_form,text='Ad-Soyad:',bg='yellow',fg='red',font='consoles 14 italic').place(x=10,y=30)
            label_tc=tk.Label(basvuru_form,text='TC No:',bg='yellow',fg='red',font='consoles 14 italic').place(x=10,y=60)
            label_modem=tk.Label(basvuru_form,text='Modem Tipi:',bg='yellow',fg='red',font='consoles 14 italic').place(x=10,y=90)
            label_arıza=tk.Label(basvuru_form,text='Arıza Tipi:',bg='yellow',fg='red',font='consoles 14 italic').place(x=10,y=120)
            label_adres=tk.Label(basvuru_form,text='Adres:',bg='yellow',fg='red',font='consoles 14 italic').place(x=10,y=150)
            label_mail=tk.Label(basvuru_form,text='Mail:',bg='yellow',fg='red',font='consoles 14 italic').place(x=10,y=180)

            entry_ad_soyad = tk.Entry(basvuru_form)
            entry_ad_soyad.place(x=130,y=35)

            entry_tc = tk.Entry(basvuru_form)
            entry_tc.place(x=130,y=65)


            liste = ['Tmp','KMNR','2TMNx','MTPL','NMPY','PNDS']
            combo_modem=Combobox(basvuru_form,values=liste).place(x=130,y=95)

            liste1=['Kablo','Giriş Hatası','Wifi Açılmıyor','İnternet Yok','NMPY','PNDS']
            combo_arıza=Combobox(basvuru_form,values=liste1).place(x=130,y=125)

            entry_adres=tk.Entry(basvuru_form)
            entry_adres.place(x=130,y=155)

            entry_mail=tk.Entry(basvuru_form)
            entry_mail.place(x=130,y=185)

            def olustur():
                #if koşullarıyla zengileştirilebilir
                msg=messagebox.showinfo('Başarıyla oluşturuldu',message='Arıza Bildiriminiz Gerçekleşti')

            buton=tk.Button(basvuru_form,text='Kayıt Oluştur',activebackground='green',command=olustur).place(x=80,y=220)






            basvuru_form.mainloop()


def iptal():
    pass


btn_giris = tk.Button(form,text='Giriş',activebackground='green',command=giris)
btn_iptal = tk.Button(form,text='iptal',activebackground='red',command=iptal)

btn_giris.place(x=110,y=150,width=50)
btn_iptal.place(x=180,y=150,width=50)




form.mainloop()