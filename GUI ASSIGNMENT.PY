from tkinter import *
import mysql.connector
from tkinter import messagebox
window=Tk()

def insert():
    amit = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="employee")
    cur=amit.cursor()
    e=empid.get()
    n=name.get()
    p=post.get()
    s=salary.get()
    pd=password.get()
    gender=var1.get()
    

    
    
    
    
    q="insert into emp values(%s,%s,%s,%s,%s,%s)"
    val=(e,n,p,s,gender,pd)
    cur.execute(q,val)
    amit.commit()
    print("Inserted....!")
    messagebox.askquestion(" value inserted"," IS your all entry are correct")
    
    
    

    




empid=StringVar()
name=StringVar()
post=StringVar()
salary=StringVar()
password=StringVar()
var1=StringVar()
var1.set(1)


Label(window,text='EMPID').grid(row=0,column=0)
Entry(window,textvariable=empid).grid(row=0,column=1)
Label(window,text='NAME').grid(row=1,column=0)
Entry(window,textvariable=name).grid(row=1,column=1)
Label(window,text='POST').grid(row=2,column=0)
Entry(window,textvariable=post).grid(row=2,column=1)
Label(window,text='SALARY').grid(row=3,column=0)
Entry(window,textvariable=salary).grid(row=3,column=1)
Label(window,text="Gender").grid(row=4,column=0)
Radiobutton(window,text="MALE" ,variable=var1,value="Male").grid(row=4,column=1,padx=0)
Radiobutton(window,text="FEMALE" ,variable=var1,value="female").grid(row=4,column=2,padx=0)
Label(window,text='Password').grid(row=5,column=0)
Entry(window,textvariable=password).grid(row=5,column=1)
Button(text="insert",command=insert).grid(row=6,column=1)

window.mainloop()
