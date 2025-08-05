import tkinter as tk

form = tk.Tk()
form.title('Kullanıcı Giriş Arayüzü')
form.geometry('500x500+350+75')
form.configure(bg='white')


mail_label = tk.Label(text='Mail :', fg='black', bg='white', font='Times 12 bold')
mail_label.place(x=10, y=30)

sifre_label = tk.Label(text='Şifre :', fg='black', bg='white', font='Times 12 bold')
sifre_label.place(x=10, y=60)

mail_entry = tk.Entry()
mail_entry.place(x=70, y=35)

sifre_entry = tk.Entry(show='*')
sifre_entry.place(x=70, y=65)

def giris():
    mail_entry.delete(0, 'end')
    sifre_entry.delete(0, 'end')

# Kayıt Kutuları Önceden Oluşturuluyor !!
ad_label = tk.Label(text='Ad :', fg='black', bg='white', font='Times 12 bold')
ad_label.place(x=10, y=130)
ad_label.place_forget()

kayit_mail_label = tk.Label(text='Mail :', fg='black', bg='white', font='Times 12 bold')
kayit_mail_label.place(x=10, y=160)
kayit_mail_label.place_forget()

kayit_sifre_label = tk.Label(text='Şifre :', fg='black', bg='white', font='Times 12 bold')
kayit_sifre_label.place(x=10, y=190)
kayit_sifre_label.place_forget()

ad_entry = tk.Entry()
ad_entry.place(x=70, y=135)
ad_entry.place_forget()

kayit_mail_entry = tk.Entry()
kayit_mail_entry.place(x=70, y=165)
kayit_mail_entry.place_forget()

kayit_sifre_entry = tk.Entry(show='*')
kayit_sifre_entry.place(x=70, y=195)
kayit_sifre_entry.place_forget()

def kayıtOl():
    
    ad_label.place(x=10, y=130)
    kayit_mail_label.place(x=10, y=160)
    kayit_sifre_label.place(x=10, y=190)

    ad_entry.place(x=70, y=135)
    kayit_mail_entry.place(x=70, y=165)
    kayit_sifre_entry.place(x=70, y=195)


kayıtol_buton = tk.Button(form, text='Kayıt Ol', fg='red', bg='white', command=kayıtOl)
kayıtol_buton.place(x=70, y=90)

giris_buton = tk.Button(form, text='Giriş', fg='red', bg='white', command=giris)
giris_buton.place(x=140, y=90)

form.mainloop()
