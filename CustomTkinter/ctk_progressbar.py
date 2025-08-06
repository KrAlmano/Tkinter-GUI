from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()
root.title("ProgressBar")
root.geometry("500x500+350+75")


def clicker():
    my_progressbar.step()
    my_label.configure(text=int((my_progressbar.get())*100))


def start():
    my_progressbar.start()
    


def stop():
    my_progressbar.stop()


my_progressbar= ctk.CTkProgressBar(root,orientation="horizontal",
                                   width=200,
                                   height=50,
                                   corner_radius=1,
                                   border_width=2,
                                   border_color="red",
                                   fg_color="white",
                                   mode="determinate",
                                   progress_color="black",
                                   determinate_speed=.5,
                                   indeterminate_speed=5)
my_progressbar.pack(pady=20)

#Set the default progress starting point
my_progressbar.set(0)

my_button=ctk.CTkButton(root,text="Click",command=clicker)
my_button.pack(pady=10)

start_button = ctk.CTkButton(root,text="Start",command=start)
start_button.pack(pady=10)

stop_button = ctk.CTkButton(root,text="Stop",command=stop)
stop_button.pack(pady=10)

my_label=ctk.CTkLabel(root,text="",font=("Helvetica",20))
my_label.pack(pady=10)



root.mainloop()