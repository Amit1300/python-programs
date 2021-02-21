import mysql.connector
import tkinter as tk 


def db():
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="employee")  
    cur=  myconn.cursor()
    
    e=empid.get()
    n=name.get()
    p=post.get()
    s=salary.get()
    q="insert into emp values(%s,%s,%s,%s)"
    val=(e,n,p,s)
    cur.execute(q,val)
    myconn.commit()
    print("Inserted....!")
    


win = tk.Tk() 
win.title('Counting Seconds')
empid=tk.StringVar()
name=tk.StringVar()
post=tk.StringVar()
salary=tk.StringVar()




lbl1=tk.Label(win,text="Emp Id")
tf1=tk.Entry(win,width=10,textvariable=empid)
lbl2=tk.Label(win,text="Name")
tf2=tk.Entry(win,width=10,textvariable=name)
lbl3=tk.Label(win,text="Post")
tf3=tk.Entry(win,width=10,textvariable=post)
lbl4=tk.Label(win,text="Salary")
tf4=tk.Entry(win,width=10,textvariable=salary)
button = tk.Button(win, text='Insert', width=25, command=db) 
lbl1.grid(row=0,column=1)
tf1.grid(row=0,column=2)
lbl2.grid(row=1,column=1)
tf2.grid(row=1,column=2)
lbl3.grid(row=2,column=1)
tf3.grid(row=2,column=2)
lbl4.grid(row=3,column=1)
tf4.grid(row=3,column=2)
button.grid(row=4,column=2)
win.mainloop() 

