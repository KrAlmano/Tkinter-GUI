import customtkinter as ctk
from PIL import Image




ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("500x600+350+100")


main_frame=ctk.CTkFrame(master=root,width=450,height=570,border_width=2,border_color="silver",corner_radius=10)


heading_label = ctk.CTkLabel(main_frame,text="Student Registiration System",font=("Bold",20),
                             width=400,height=30,
                             bg_color="silver",text_color="black")
heading_label.place(x=23,y=2)

add_picture_frame = ctk.CTkFrame(main_frame,width=100,height=100,
                                 border_width=1,border_color="white",corner_radius=6)


profile_template_pic = ctk.CTkImage(Image.open('avatar_default.png'),size=(83,82))


add_picture_button = ctk.CTkButton(add_picture_frame,text="",width=0,height=0,
                                   image=profile_template_pic,fg_color="transparent")
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
select_gender_label.place(x=40,y=220)

student_gender = ctk.StringVar()


male_gender_button = ctk.CTkRadioButton(main_frame,text="Male",variable=student_gender,value="Male")
male_gender_button.place(x=190,y=223)

female_gender_button = ctk.CTkRadioButton(main_frame,text="Female",variable=student_gender,value="Female")
female_gender_button.place(x=280,y=223)





main_frame.place(x=25,y=10)







root.mainloop()