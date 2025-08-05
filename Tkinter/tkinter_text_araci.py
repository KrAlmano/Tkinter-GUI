import tkinter as tk

form = tk.Tk()
form.geometry('500x500+350+75')
form.title('Text Aracı')
form.config(bg='pink')

text=tk.Text(form,width=20,height=20,padx=10,pady=10,bd=10,
             selectbackground='green',font='Times 12 bold').pack()


#Width,height genişlik
#padx, pady metnin kenarlardan uzaklıkları
#bd çerçeve
#selectbackground seçilen metnin arka plan rengi


form.mainloop()