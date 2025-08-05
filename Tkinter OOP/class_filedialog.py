from tkinter import *
from tkinter import ttk,filedialog


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("OOP File Dialog")
        photo = PhotoImage(file="deneme.png")
        self.iconphoto(False,photo)
        self.geometry("500x500+350+75")
        

        #Create Widgets

        self.my_text = Text(self,width=80,height=10)
        self.my_text.pack(pady=20)

        self.my_button = ttk.Button(self,text="Open file",command=self.file)
        self.my_button.pack(pady=20)


    def file(self):
        self.my_file = filedialog.askopenfilename(initialdir="",
                                                  title= "Select a file",
                                                  filetypes=(("txt files","*.txt"),("All Files","*.*")))
        
        #Check to make sure user selected a file
        if self.my_file:
            #Open and read the file 
            get_contents= open(self.my_file,"r")
            self.my_text.insert(END,get_contents.read())





app= App()
app.mainloop()