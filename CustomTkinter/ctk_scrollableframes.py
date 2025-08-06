from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Scrollable Frames")
root.geometry("400x400+400+100")

#Create a scrollable frame

my_frame = ctk.CTkScrollableFrame(root,orientation="vertical",
                                  width=330,
                                  height=230,
                                  label_text="Hello world",
                                  label_fg_color="pink",
                                  label_text_color="white",
                                  label_font=("Helvetica",18),
                                  label_anchor="n", #center,n,ne,nw,s,se,sw,w,e
                                  border_width=3,
                                  border_color="yellow",
                                  fg_color="black")
my_frame.pack(pady=40)


#for loop for buttons
for x in range(20):
    ctk.CTkButton(my_frame,text="Button",fg_color="white",text_color="black").pack(pady=10)


root.mainloop()