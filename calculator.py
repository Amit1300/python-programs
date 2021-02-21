from tkinter import*
window=Tk()
window.title("AMIT NAGAR CALCULATOR")
window.config(bg="yellow")
window.geometry("270x150")

def add():
    x=e.get()
    x1=e1.get()
    return(int(x)+int(x1))

def sub():
    x=e.get()
    x1=e1.get()
    print(x)
    if x1>x:
        return(int(x1)-int(x))
    else:
        return(int(x)-int(x1))
    
    
def div():
    x=e.get()
    x1=e1.get()
    return(int(x)/int(x1))

def mul():
    x=e.get()
    x1=e1.get()
    return(int(x)*int(x1))

def result():
        f3.set(add())

def clear():
    f3.set("")


   

f1=StringVar()

e=Entry(window,textvariable=f1)
e.grid(padx=3,row=0,column=1)
label=Label(text="input value").grid(row=0,column=0)

f3=StringVar()
e2=Entry(window,textvariable=f3)
e2.grid(padx=3,row=3,column=1)
label=Label(text="RESULT").grid(row=3,column=0)

b=Button(text="result",command=result).grid()
c=Button(text="clear",command=clear).grid()



f2=StringVar()

e1=Entry(window,textvariable=f2)
e1.grid(padx=3,row=1,column=1)
label=Label(text="input value2").grid(row=1,column=0)
button1=Button(text="add", command=add).grid(row=2,column=5)
button2=Button(text="sub", command=sub).grid(row=2,column=4)
button3=Button(text="div", command=div).grid(row=2,column=2)
button4=Button(text="mul", command=mul).grid(row=2,column=3)

menu=Menu(window)
m1=Menu(menu)
m1.add_command(label="open")
m1.add_command(label="save")
m1.add_command(label="save as")
m1.add_command(label="exit")
window.config(menu=menu)
menu.add_cascade(label="file",menu=m1)


m1=Menu(menu)
m1.add_command(label="open")
m1.add_command(label="save")
m1.add_command(label="save as")
m1.add_command(label="exit")
window.config(menu=menu)
menu.add_cascade(label="file",menu=m1)
















window.mainloop()
