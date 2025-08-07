import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
from tkinter.filedialog import askopenfile
import customtkinter as ctk

class StudentRegistrationApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("Öğrenci Kayıt Sistemi")
        self.geometry("500x650+350+100")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")     
        self.student_database = []    
        self._create_widgets()

    def _create_widgets(self):
        
        self.main_frame = ctk.CTkFrame(master=self, width=450, height=630, border_width=2, border_color="silver", corner_radius=10)
        self.main_frame.place(x=25, y=10)
  
        heading_label = ctk.CTkLabel(self.main_frame, text="Student Registration System", font=("Bold", 20),
                                     width=400, height=30, bg_color="silver", text_color="black")
        heading_label.place(x=23, y=2)
 
        add_picture_frame = ctk.CTkFrame(self.main_frame, width=100, height=100,
                                         border_width=1, border_color="white", corner_radius=6)
        add_picture_frame.place(x=320, y=70)

        try:
            profile_template_pic = ctk.CTkImage(Image.open('avatar_default.png'), size=(83, 82))
        except FileNotFoundError:
            profile_template_pic = ctk.CTkImage(Image.new('RGB', (83, 82), 'gray'), size=(83, 82))
            
        self.add_picture_button = ctk.CTkButton(add_picture_frame, text="", width=0, height=0,
                                                image=profile_template_pic, fg_color="transparent", command=self.ask_open_pp)
        self.add_picture_button.place(x=5, y=5)

        
        self.student_id_number_entry = ctk.CTkEntry(self.main_frame, font=("Bold", 15),
                                                    width=220, placeholder_text="Enter Student ID Number")
        self.student_id_number_entry.place(x=20, y=70)

        self.student_full_name_entry = ctk.CTkEntry(self.main_frame, font=("Bold", 15),
                                                    width=220, placeholder_text="Enter Full Name")
        self.student_full_name_entry.place(x=20, y=120)

        self.student_age_entry = ctk.CTkEntry(self.main_frame, font=("Bold", 15),
                                              width=220, placeholder_text="Enter Your Age")
        self.student_age_entry.place(x=20, y=170)

        
        select_gender_label = ctk.CTkLabel(self.main_frame, text="Select Gender:", font=("Bold", 17))
        select_gender_label.place(x=20, y=220)
        self.student_gender = tk.StringVar()
        male_gender_button = ctk.CTkRadioButton(self.main_frame, text="Male", variable=self.student_gender, value="Male")
        male_gender_button.place(x=210, y=223)
        female_gender_button = ctk.CTkRadioButton(self.main_frame, text="Female", variable=self.student_gender, value="Female")
        female_gender_button.place(x=280, y=223)

       
        select_student_class_label = ctk.CTkLabel(self.main_frame, text="Select Student Class :", font=("Bold", 17))
        select_student_class_label.place(x=20, y=260)
        classes = ["1st", "2nd", "3rd", "4th", "5th"]
        self.select_student_class_combobox = ctk.CTkComboBox(self.main_frame, values=classes, state="readonly")
        self.select_student_class_combobox.place(x=210, y=260)
        self.select_student_class_combobox.set("Select Class")

        
        register_button = ctk.CTkButton(self.main_frame, text="Register", fg_color="green",
                                        text_color="black", font=("Bold", 20), width=100, command=self.register_student)
        register_button.place(x=20, y=320)

        update_button = ctk.CTkButton(self.main_frame, text="Update", fg_color="yellow",
                                      text_color="black", font=("Bold", 20), width=100, command=self.update_student)
        update_button.place(x=130, y=320)

        clear_button = ctk.CTkButton(self.main_frame, text="Clear", fg_color="orange",
                                     text_color="black", font=("Bold", 20), width=100, command=self.clear_fields)
        clear_button.place(x=240, y=320)

        
        self.find_by_student_entry = ctk.CTkEntry(self.main_frame, font=("Bold", 15), width=180,
                                                  placeholder_text="Find Student")
        self.find_by_student_entry.place(x=20, y=370)

        find_by_options = ["ID", "Name", "Class"]
        self.find_by_student_option_box = ctk.CTkComboBox(self.main_frame, state="readonly", values=find_by_options)
        self.find_by_student_option_box.place(x=210, y=370)
        self.find_by_student_option_box.set("Find By")
        
        find_button = ctk.CTkButton(self.main_frame, text="Find", width=60, command=self.find_student)
        find_button.place(x=370, y=370)

       
        theme_configuration = {
            "Treeview": {
                "configure": {"background": "gray17", "foreground": "white", "fieldbackground": "gray17", "font": ("Segoe UI", 10), "rowheight": 20, "borderwidth": 0},
                "map": {"background": [("selected", "#0078D7")], "foreground": [("selected", "white")]}
            },
            "Treeview.Heading": {
                "configure": {"background": "gray25", "foreground": "white", "font": ("Segoe UI", 12, "bold"), "padding": (10, 10), "relief": "flat"},
                "map": {"background": [("active", "gray35")], "foreground": [("active", "white")]}
            }
        }
        style = ttk.Style()
        style.theme_create(themename="custom", parent="clam", settings=theme_configuration)
        style.theme_use(themename="custom")

        self.records_table = ttk.Treeview(self.main_frame, columns=("ID", "Name", "Age", "Gender", "Class"), show="headings")
        self.records_table.column("ID", width=80, anchor="w")
        self.records_table.heading("ID", text="ID Number", anchor="center")
        self.records_table.column("Name", width=120, anchor="w")
        self.records_table.heading("Name", text="Name", anchor="center")
        self.records_table.column("Age", width=50, anchor="center")
        self.records_table.heading("Age", text="Age", anchor="center")
        self.records_table.column("Gender", width=60, anchor="center")
        self.records_table.heading("Gender", text="Gender", anchor="center")
        self.records_table.column("Class", width=60, anchor="center")
        self.records_table.heading("Class", text="Class", anchor="center")
        self.records_table.place(x=40, y=650, width=600, height=210)
        self.records_table.bind("<<TreeviewSelect>>", self.select_record)

       
        clear_selection_button = ctk.CTkButton(self.main_frame, text="Clear Selection", width=120, fg_color="orange",
                                               text_color="black", font=("Bold", 16), command=self.clear_selection)
        clear_selection_button.place(x=30, y=580)

        delete_record_button = ctk.CTkButton(self.main_frame, text="Delete Record", width=120, fg_color="red",
                                             text_color="black", font=("Bold", 16), command=self.delete_record)
        delete_record_button.place(x=160, y=580)
        
        show_all_button = ctk.CTkButton(self.main_frame, text="Show All", width=120,
                                             text_color="white", font=("Bold", 16), command=self.show_all_students)
        show_all_button.place(x=290, y=580)

    

    def ask_open_pp(self):
        ask_open_file = askopenfile()
        if ask_open_file:
             profile_picture_path = ask_open_file.name
             profile_picture__image_obj = ctk.CTkImage(Image.open(profile_picture_path),size=(80,80))

             self.add_picture_button.configure(image = profile_picture__image_obj)
             self.add_picture_button.image = profile_picture__image_obj

    def _update_treeview(self, data_source):
        self.records_table.delete(*self.records_table.get_children())
        for record in data_source:
            self.records_table.insert("", "end", values=record)

    def clear_fields(self):
        self.student_id_number_entry.delete(0, "end")
        self.student_full_name_entry.delete(0, "end")
        self.student_age_entry.delete(0, "end")
        self.student_gender.set("")
        self.select_student_class_combobox.set("Select Class")
        self.student_id_number_entry.focus()

    def clear_selection(self):
        self.clear_fields()
        if self.records_table.selection():
            self.records_table.selection_remove(self.records_table.selection())

    def select_record(self, event=None):
        self.clear_fields()
        selected_item = self.records_table.focus()
        if not selected_item: return
        values = self.records_table.item(selected_item, "values")
        self.student_id_number_entry.insert(0, values[0])
        self.student_full_name_entry.insert(0, values[1])
        self.student_age_entry.insert(0, values[2])
        self.student_gender.set(values[3])
        self.select_student_class_combobox.set(values[4])

    def register_student(self):
        student_id = self.student_id_number_entry.get()
        name = self.student_full_name_entry.get()
        age = self.student_age_entry.get()
        gender = self.student_gender.get()
        student_class = self.select_student_class_combobox.get()

        if not all([student_id, name, age, gender, student_class != "Select Class"]):
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
            return
        for student in self.student_database:
            if student[0] == student_id:
                messagebox.showerror("Hata", f"{student_id} numaralı öğrenci zaten kayıtlı.")
                return
        data = (student_id, name, age, gender, student_class)
        self.student_database.append(data)
        self._update_treeview(self.student_database)
        self.clear_fields()
        messagebox.showinfo("Başarılı", "Öğrenci başarıyla kaydedildi.")

    def update_student(self):
        selected_item = self.records_table.focus()
        if not selected_item:
            messagebox.showerror("Hata", "Lütfen güncellenecek bir kayıt seçin.")
            return
        student_id = self.student_id_number_entry.get()
        name = self.student_full_name_entry.get()
        age = self.student_age_entry.get()
        gender = self.student_gender.get()
        student_class = self.select_student_class_combobox.get()
        if not all([student_id, name, age, gender, student_class != "Select Class"]):
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
            return
        original_id = self.records_table.item(selected_item, "values")[0]
        for i, student in enumerate(self.student_database):
            if student[0] == original_id:
                self.student_database[i] = (student_id, name, age, gender, student_class)
                break
        self._update_treeview(self.student_database)
        self.clear_fields()
        messagebox.showinfo("Başarılı", "Kayıt başarıyla güncellendi.")

    def delete_record(self):
        selected_item = self.records_table.focus()
        if not selected_item:
            messagebox.showerror("Hata", "Lütfen silinecek bir kayıt seçin.")
            return
        if messagebox.askyesno("Onay", "Bu kaydı silmek istediğinizden emin misiniz?"):
            original_id = self.records_table.item(selected_item, "values")[0]
            self.student_database = [s for s in self.student_database if s[0] != original_id]
            self._update_treeview(self.student_database)
            self.clear_fields()
            messagebox.showinfo("Başarılı", "Kayıt silindi.")

    def find_student(self):
        """Arama yapar ve sonucu tabloda gösterir. Sonuç yoksa tabloyu değiştirmez."""
        search_term = self.find_by_student_entry.get().lower()
        search_by = self.find_by_student_option_box.get()
        if not search_term or search_by == "Find By":
            messagebox.showwarning("Uyarı", "Lütfen arama terimi ve kriteri seçin.")
            return
        
        column_map = {"ID": 0, "Name": 1, "Class": 4}
        search_index = column_map.get(search_by)
        
        results = [student for student in self.student_database if search_term in str(student[search_index]).lower()]
        
       
        if results:
            self._update_treeview(results)
        else:
            
            messagebox.showinfo("Sonuç Yok", "Arama kriterlerine uygun kayıt bulunamadı.")

    def show_all_students(self):
        """Tüm kayıtları tekrar tabloda gösterir."""
        self._update_treeview(self.student_database)
        self.find_by_student_entry.delete(0, "end")


if __name__ == "__main__":
    app = StudentRegistrationApp()
    app.mainloop()
