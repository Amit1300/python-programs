#harry practice
from tkinter import*
from tkinter import messagebox 

top=Tk()
top.title(" hi i m AMIT")

def help():
       x=" hi I M AMIT .i m here to help you"
       y=messagebox.askquestion("Information",x)
       if y=="yes":
           messagebox.showinfo("x","thank you")
       else:
           pass
       
def get():
        messagebox.askokcancel("dollars",f" here we r ving you {scale.get()}")
        

mymenu=Menu(top)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label="file")
m1.add_command(label="save")
m1.add_command(label="save as")
m1.add_command(label="exit")

top.config(menu=mymenu)
mymenu.add_cascade(label="open" ,menu=m1)


#mymenu=Menu(top)
m2=Menu(mymenu,tearoff=0)
m2.add_command(label="help ", command=help)


top.config(menu=mymenu)
mymenu.add_cascade(label="help gui" ,menu=m2)

scale=Scale(top,from_=0, to=100,orient = HORIZONTAL)
scale.pack()

Button(text="click" ,command=get).pack()








top.mainloop()
