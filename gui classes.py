#gui class
from tkinter import *
class GUI(Tk):
    def __init__(self):
        super().__init__()

    def status(self):
        self.var=StringVar()
        self.var.set('READY')
        self.statusbar=Label(self,textvariable=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack()

    def click(self):
        print("hello  i m amit")
        
    def createbutton(self,intext):
        Button(text=intext,command=self.click).pack()
window=GUI()
window.status()
window.createbutton("rd")
    
    
