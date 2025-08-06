from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Textbox Editor")
root.geometry("600x400+400+90")

clipboard_content = ''

def delete_all_text():
    """Metin kutusundaki tüm metni siler."""
    my_text.delete("0.0", "end")
    status_label.configure(text="Tüm metin silindi.")

def copy_text():
    """Sadece seçili metni kopyalar."""
    global clipboard_content
    try:
       
        clipboard_content = my_text.selection_get()
        status_label.configure(text="Seçim kopyalandı!")
    except:
        
        clipboard_content = ''
        status_label.configure(text="Kopyalanacak metin seçilmedi.")

def cut_text():
    """Seçili metni keser (kopyalar ve siler)."""
    global clipboard_content
    try:
        clipboard_content = my_text.selection_get()
        
        my_text.delete("sel.first", "sel.last")
        status_label.configure(text="Seçim kesildi!")
    except:
        clipboard_content = ''
        status_label.configure(text="Kesilecek metin seçilmedi.")

def paste_text():
    """Kopyalanan metni imlecin olduğu yere yapıştırır."""
    if clipboard_content:
       
        my_text.insert(ctk.INSERT, clipboard_content)
        status_label.configure(text="Metin yapıştırıldı.")
    else:
        status_label.configure(text="Yapıştırılacak bir şey yok.")

my_text = ctk.CTkTextbox(root,
                         width=500, height=250,
                         corner_radius=10,
                         border_width=2,
                         wrap="word",
                         font=("Helvetica", 14))
my_text.pack(pady=20, padx=20)

my_frame = ctk.CTkFrame(root, fg_color="transparent")
my_frame.pack(pady=10)

cut_button = ctk.CTkButton(my_frame, text="Kes", command=cut_text)
copy_button = ctk.CTkButton(my_frame, text="Kopyala", command=copy_text)
paste_button = ctk.CTkButton(my_frame, text="Yapıştır", command=paste_text)
delete_button = ctk.CTkButton(my_frame, text="Tümünü Sil", command=delete_all_text, fg_color="#D32F2F", hover_color="#B71C1C")

cut_button.grid(row=0, column=0, padx=5)
copy_button.grid(row=0, column=1, padx=5)
paste_button.grid(row=0, column=2, padx=5)
delete_button.grid(row=0, column=3, padx=5)


status_label = ctk.CTkLabel(root, text="Başlamak için bir metin yazın...", text_color="gray")
status_label.pack(pady=10)

root.mainloop()


