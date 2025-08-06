from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Switch")
root.geometry("400x300+400+90")

def click():
    my_label.configure(text="Tab1 view")

my_tab = ctk.CTkTabview(root,
                        width=600,
                        height=250,
                        corner_radius=10,
                        fg_color="silver",
                        segmented_button_fg_color="red",
                        segmented_button_selected_color="green",
                        segmented_button_selected_hover_color="pink",
                        segmented_button_unselected_color="purple"
                        ,segmented_button_unselected_hover_color="yellow",
                        text_color="white")
my_tab.pack(pady=10)

#Create tabs
tab_1=my_tab.add("Tab 1") 
tab_2=my_tab.add("Tab 2")

#Put stuff in tabs
my_button = ctk.CTkButton(tab_1,text="Print",command=click)
my_button.pack(pady=10)


my_label = ctk.CTkLabel(tab_1,text="",text_color="black")
my_label.pack()



root.mainloop()