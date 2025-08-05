from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        super().__init__()

        # Pencere Başlığı, İkonu ve Boyutu
        self.title("Calculator")
        self.geometry("400x500+420+110")
        self.resizable(False, False) # Pencere boyutunun değiştirilmesini engelle
        photo = PhotoImage(file="calculator.png")
        self.iconphoto(False,photo)

        # TTK Stili oluşturma ve yapılandırma
        style = ttk.Style(self)
        style.configure('TButton', font=('Helvetica', 18), padding=10)
        style.configure('Clear.TButton', foreground='red') # Clear butonu için özel stil

        # Widget'ları oluşturma
        self.my_label = Label(self, text="", font="Helvatica 20")
        self.my_label.pack(pady=(20, 10), padx=10, fill='x')
        self.my_entry = Entry(self, width=20, font="Helvetica 24", justify='right', bd=2, relief='solid')
        self.my_entry.pack(pady=(0, 20), padx=10, ipady=10, fill='x')

        # Düğmeleri tutacak olan Frame'i oluşturma
        My_frame(self)

    def clear(self):
        """
        Giriş kutusunu ve etiketi temizler.
        """
        self.my_entry.delete(0, END)
        self.my_label.config(text="")
    
    def pos_neg(self):
        """
        Sayıyı pozitif veya negatife çevirir.
        """
        if self.my_entry.get():
            try:
                # Girişte sadece bir sayı olduğundan emin ol
                if "+" not in self.my_entry.get() and "-" not in self.my_entry.get()[1:] and "*" not in self.my_entry.get() and "/" not in self.my_entry.get():
                    number_str = self.my_entry.get()
                    if "." in number_str:
                        number = float(number_str)
                    else:
                        number = int(number_str)
                    
                    self.my_entry.delete(0, END)
                    self.my_entry.insert(0, -1 * number)
            except ValueError:
                # Geçersiz bir format varsa hiçbir şey yapma
                pass

    def num_press(self, num):
        """
        Bir sayı düğmesine basıldığında sayıyı giriş kutusuna ekler.
        """
        self.my_entry.insert(END, num)

    def signage(self, sign):
        """
        Bir işlem işaretine basıldığında işareti giriş kutusuna ekler.
        """
        if self.my_entry.get():
            self.my_entry.insert(END, sign)

    def mather(self):
        """
        Matematiksel işlemi gerçekleştirir.
        """
        if self.my_entry.get():
            try:
                equation = self.my_entry.get()
                # eval() güvenlik riski oluşturabilir, ancak bu basit uygulama için kullanılmıştır.
                result = eval(equation)
                
                # Etiketi güncelle
                self.my_label.config(text=f'{equation} = {result}')
                
                # Giriş kutusunu temizle ve sonucu yaz
                self.my_entry.delete(0, END)
                self.my_entry.insert(0, result)
            except (SyntaxError, NameError, ZeroDivisionError) as e:
                # Hata durumunda etiketi güncelle
                self.my_label.config(text="Hatalı İfade")
                self.my_entry.delete(0, END)


class My_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Frame'i paketle
        self.pack(padx=10, pady=10)

        # Düğmeleri tanımla (ttk.Button kullanarak)
        # Her düğmenin aynı boyutta olmasını sağlamak için 'sticky' kullanılır.
        # 'weight' ayarı, pencere boyutu değişirse sütunların nasıl genişleyeceğini belirler.
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Düğmeleri oluşturma ve grid'e yerleştirme
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('+/-', 3, 0), ('0', 3, 1), ('.', 3, 2), ('+', 3, 3),
        ]

        for (text, row, col) in buttons:
            if text.isdigit() or text == '.':
                cmd = lambda t=text: parent.num_press(t)
            elif text in ['/', '*', '-', '+']:
                cmd = lambda t=text: parent.signage(t)
            elif text == '+/-':
                cmd = parent.pos_neg
            
            ttk.Button(self, text=text, command=cmd).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # Clear ve Equal butonları için özel yerleşim
        ttk.Button(self, text="Clear", command=parent.clear, style='Clear.TButton').grid(row=4, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(self, text="=", command=parent.mather).grid(row=4, column=2, columnspan=2, sticky="nsew", padx=2, pady=2)


if __name__ == "__main__":
    app = App()
    app.mainloop()
