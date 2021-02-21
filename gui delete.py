from tkinter import *
import mysql.connector
from tkinter import messagebox
window=Tk()

def delete():
    amit = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="employee")
    cur=amit.cursor()
    e=empid.get()
    n=name.get()
    p=post.get()
    q="delete from emp where empid='456'"
    cur.execute(q)
    amit.commit()
    print("Deleted....!")
    messagebox.askquestion(" value deleted"," are you sure u want to delete")
    
    

def ok():
    amit = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="employee")
    cur=amit.cursor()
    s="select * from emp "
    cur.execute(s)
    e=empid.get()
    record=cur.fetchall()
    print(record)
    print(record[0][1])
    for x in record:
        if e==x[0]:
            name.set(x[1])
            post.set(x[2])
            print(x[1][1])
        else:
            messagebox.showinfo('datamissmatch', "error")
    
    




empid=StringVar()
name=StringVar()
post=StringVar()


Label(window,text='EMPID').grid(row=0,column=0)
Entry(window,textvariable=empid).grid(row=0,column=1)
Label(window,text='NAME').grid(row=1,column=0)
Entry(window,textvariable=name).grid(row=1,column=1)
Label(window,text='POST').grid(row=2,column=0)
Entry(window,textvariable=post).grid(row=2,column=1)

Button(text="OK",command=ok).grid(row=0,column=3)
Button(text="delete",command=delete).grid(row=6,column=1)

window.mainloop()
