import customtkinter as ctk
from PIL import Image
from tkinter.ttk import Treeview,Style
from tkinter.filedialog import askopenfile
from tkinter import messagebox



ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("500x600+350+100")


def ask_open_pp():
    ask_open_file = askopenfile()
    if ask_open_file:
        profile_picture_path = ask_open_file.name
        profile_picture__image_obj = ctk.CTkImage(Image.open(profile_picture_path),size=(80,80))

        add_picture_button.configure(image = profile_picture__image_obj)
        add_picture_button.image = profile_picture__image_obj
     


main_frame=ctk.CTkFrame(master=root,width=450,height=570,border_width=2,border_color="silver",corner_radius=10)


heading_label = ctk.CTkLabel(main_frame,text="Student Registiration System",font=("Bold",20),
                             width=400,height=30,
                             bg_color="silver",text_color="black")
heading_label.place(x=23,y=2)

add_picture_frame = ctk.CTkFrame(main_frame,width=100,height=100,
                                 border_width=1,border_color="white",corner_radius=6)


profile_template_pic = ctk.CTkImage(Image.open('avatar_default.png'),size=(83,82))


add_picture_button = ctk.CTkButton(add_picture_frame,text="",width=0,height=0,
                                   image=profile_template_pic,fg_color="transparent",command=ask_open_pp)
add_picture_button.place(x=5,y=5)

add_picture_frame.place(x=320,y=70)

student_id_number_entry= ctk.CTkEntry(main_frame,font=("Bold",15),
                                      width=220,placeholder_text="Enter Student ID Number")

student_id_number_entry.place(x=20,y=70)


student_full_name_entry= ctk.CTkEntry(main_frame,font=("Bold",15),
                                      width=220,placeholder_text="Enter Full Name")

student_full_name_entry.place(x=20,y=120)


student_age_entry= ctk.CTkEntry(main_frame,font=("Bold",15),
                                      width=220,placeholder_text="Enter Your Age")

student_age_entry.place(x=20,y=170)


select_gender_label = ctk.CTkLabel(main_frame,text="Select Gender:",font=("Bold",17))
select_gender_label.place(x=20,y=220)

student_gender = ctk.StringVar()


male_gender_button = ctk.CTkRadioButton(main_frame,text="Male",variable=student_gender,value="Male")
male_gender_button.place(x=210,y=223)

female_gender_button = ctk.CTkRadioButton(main_frame,text="Female",variable=student_gender,value="Female")
female_gender_button.place(x=280,y=223)


select_student_class_label = ctk.CTkLabel(main_frame,text="Select Student Class :",font=("Bold",17))
select_student_class_label.place(x=20,y= 260)

classes = ["1st","2nd","3rd","4th","5th"]

select_student_class_combobox = ctk.CTkComboBox(main_frame,values=classes,state="readonly")
select_student_class_combobox.place(x=210,y=260)
select_student_class_combobox.set("Select Class")


register_button = ctk.CTkButton(main_frame,text="Register",fg_color="green",
                                text_color="black",font=("Bold",20),width=100)
register_button.place(x=20,y=320)

update_button = ctk.CTkButton(main_frame,text="Update",fg_color="yellow",
                                text_color="black",font=("Bold",20),width=100)
update_button.place(x=130,y=320)

clear_button = ctk.CTkButton(main_frame,text="Clear",fg_color="orange",
                                text_color="black",font=("Bold",20),width=100)
clear_button.place(x=240,y=320)


find_by_student_entry = ctk.CTkEntry(main_frame,font=("Bold",15),width=180,
                                     placeholder_text="Find Student")
find_by_student_entry.place(x=20,y=370)

find_by_options= ["ID","Name","Class"]

find_by_student_option_box = ctk.CTkComboBox(main_frame,state="readonly",
                                             values=find_by_options)

find_by_student_option_box.place(x=210,y=370)
find_by_student_option_box.set("Find By")

theme_configuration = {
    "Treeview": {
        "configure": {
            "background": "gray17",       # Ana gövde arkaplan rengi
            "foreground": "white",         # Ana metin rengi
            "fieldbackground": "gray17",   # Alan arkaplanı (gövde ile aynı)
            "font": ("Segoe UI", 10),       # Satır fontu
            "rowheight": 20,               # Her bir satırın yüksekliği
            "borderwidth": 0               # Kenarlık olmasın
        },
        "map": {
            # 'selected' durumu için stil ayarları (bir satır seçildiğinde)
            "background": [("selected", "#0078D7")], # Seçili satır arkaplanı (canlı mavi)
            "foreground": [("selected", "white")]    # Seçili satır metin rengi
        }
    },
    "Treeview.Heading": {
        "configure": {
            "background": "gray25",       # Başlıkların arkaplanı
            "foreground": "white",         # Başlık metin rengi
            "font": ("Segoe UI", 12, "bold"), # Başlık fontu (kalın)
            "padding": (10, 10),           # Başlık içi boşluk (sol/sağ, üst/alt)
            "relief": "flat"               # Kenarlık stili (düz)
        },
        "map": {
            # 'active' durumu için stil ayarları (fare başlığın üzerindeyken)
            "background": [("active", "gray35")],
            "foreground": [("active", "white")]
        }
    }
}


style = Style()
style.theme_create(themename="custom",parent="clam",settings=theme_configuration)
style.theme_use(themename="custom")

records_table = Treeview(main_frame,columns=("İd","name","age","gender","class"),
                         show="headings")

records_table.column(column="İd",width=80,anchor="w")
records_table.heading(column="İd",text="ID Number",anchor="center")

records_table.column(column="name",width=120,anchor="w")
records_table.heading(column="name",text="Name",anchor="center")


records_table.column(column="age",width=80,anchor="w")
records_table.heading(column="age",text="Age",anchor="center")

records_table.column(column="gender",width=80,anchor="w")
records_table.heading(column="gender",text="Gender",anchor="center")


records_table.column(column="class",width=80,anchor="w")
records_table.heading(column="class",text="Class",anchor="center")

records_table.place(x=20,y=615,width=600,height=160)


clear_selection_button = ctk.CTkButton(main_frame,text="Clear Selection",width=140,fg_color="orange",
                                       text_color="black",font=("Bold",20))
clear_selection_button.place(x=110,y=530)

delete_record_button = ctk.CTkButton(main_frame,text="Delete Record",width=140,fg_color="red",
                                     text_color="black",font=("Bold",20))
delete_record_button.place(x=272,y=530)




main_frame.place(x=25,y=10)




root.mainloop()