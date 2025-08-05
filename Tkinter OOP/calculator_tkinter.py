from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        super().__init__()


        #Title,icon,size

        self.title("Calculator")
        #photo = PhotoImage(file="calculator.png")
        #self.iconphoto(False,photo)
        self.geometry("400x600+420+110")

        #Create Widgets
        self.my_label=Label(self,text="",font="Helvatica 20")
        self.my_label.pack(pady=(10,0))
        self.my_entry = Entry(self,width=20,font="Helvetica 20")
        self.my_entry.pack(pady=(0,10))

        #Create a new frame to hold the button
        My_frame(self)

    def clear(self):
        #Clear the entry box
        self.my_entry.delete(0,END)
        #Clear the label
        self.my_label.config(text="")
    
    def pos_neg(self):
        """
        Flip numbers positive or negative
        """
        if self.my_entry.get():
            if self.my_entry.get().startswith("-"):
                number = int(self.my_entry.get())

                 #Delete entry box
                self.my_entry.delete(0,END)

                 #Flip the number sign +/-
                self.my_entry.insert(0,(-1) * number)
                 
           
            elif "+" not in self.my_entry.get() and "-" not in self.my_entry.get() and "*" not in self.my_entry.get()and "/" not in self.my_entry.get():       
                 #Get whatever is in the entry box
                 number = int(self.my_entry.get())

                 #Delete entry box
                 self.my_entry.delete(0,END)

                 #Flip the number sign +/-
                 self.my_entry.insert(0,(-1) * number)

    def num_press(self,num):
        self.my_entry.insert(END,num)

    #Get the math sign
    def signage(self,sign):
        #check to make sure there is stuff in the box
        if self.my_entry.get():
            #Add the sign to end of the entry box
            self.my_entry.insert(END,sign)

    #Do the math
    def mather(self):
        #Make sure the box is full
        if self.my_entry.get():
            #Define our equation
            equation = self.my_entry.get()
            #Output the equation to the label
            self.my_label.config(text=f'{equation} = {eval(equation)}')
            #Delete the box
            self.my_entry.delete(0,END)

            #Output the answer
            self.my_entry.insert(END,eval(equation))
class My_frame(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        #Pack the frame
        self.pack()
        #Define the buttons

        self.button_1 = Button(self,text="1",font="Helvetica 24",command= lambda:parent.num_press("1"))
        self.button_2 = Button(self,text="2",font="Helvetica 24",command= lambda: parent.num_press("2"))
        self.button_3 = Button(self,text="3",font="Helvetica 24",command= lambda: parent.num_press("3"))

        self.button_4 = Button(self,text="4",font="Helvetica 24",command= lambda: parent.num_press("4"))
        self.button_5 = Button(self,text="5",font="Helvetica 24",command= lambda: parent.num_press("5"))
        self.button_6 = Button(self,text="6",font="Helvetica 24",command= lambda: parent.num_press("6"))

        self.button_7 = Button(self,text="7",font="Helvetica 24",command= lambda: parent.num_press("7"))
        self.button_8 = Button(self,text="8",font="Helvetica 24",command= lambda: parent.num_press("8"))
        self.button_9 = Button(self,text="9",font="Helvetica 24",command= lambda: parent.num_press("9"))

        self.button_0 = Button(self,text="0",font="Helvetica 24",command= lambda: parent.num_press("0"))
        self.button_negative = Button(self,text="+/-",font="Helvetica 24",command=parent.pos_neg)
        self.button_equal = Button(self,text="=",font="Helvetica 24",command=parent.mather)

        self.button_plus = Button(self,text="+",font="Helvetica 24",command=lambda:parent.signage("+"))
        self.button_minus = Button(self,text="-",font="Helvetica 24",command=lambda:parent.signage("-"))
        self.button_multiply = Button(self,text="x",font="Helvetica 24",command=lambda:parent.signage("*"))
        self.button_divide = Button(self,text="/",font="Helvetica 24",command=lambda:parent.signage("/"))

        self.button_clear = Button(self,text="Clear",font="Helvetica 24",command=parent.clear,width=10)

        #Grid the buttons to the screen
        self.button_1.grid(row=0,column=0,ipadx=20,ipady=10,padx=(0,10))
        self.button_2.grid(row=0,column=1,ipadx=20,ipady=10)
        self.button_3.grid(row=0,column=2,ipadx=20,ipady=10)

        self.button_4.grid(row=1,column=0,ipadx=20,ipady=10,padx=(0,10),pady=10)
        self.button_5.grid(row=1,column=1,ipadx=20,ipady=10)
        self.button_6.grid(row=1,column=2,ipadx=20,ipady=10)

        self.button_7.grid(row=2,column=0,ipadx=20,ipady=10,padx=(0,10),pady=10)
        self.button_8.grid(row=2,column=1,ipadx=20,ipady=10)
        self.button_9.grid(row=2,column=2,ipadx=20,ipady=10,padx=(10,0),pady=10)

        self.button_0.grid(row=3,column=1,ipadx=20,ipady=10,padx=(0,10),pady=10)
        self.button_negative.grid(row=3,column=0,ipadx=10,ipady=10)
        self.button_equal.grid(row=3,column=2,ipadx=20,ipady=10,padx=(10,0),pady=10)

        self.button_plus.grid(row=0,column=3,ipadx=20,ipady=10,padx=(10,0),pady=10)
        self.button_minus.grid(row=1,column=3,ipadx=20,ipady=10,padx=(10,0),pady=10)
        self.button_multiply.grid(row=2,column=3,ipadx=20,ipady=10,padx=(10,0),pady=10)
        self.button_divide.grid(row=3,column=3,ipadx=20,ipady=10,padx=(10,0),pady=10)

        self.button_clear.grid(row=5,column=1,columnspan=2 ,ipadx=40,ipady=10,padx=(10,0))





app = App()
app.mainloop()
        
