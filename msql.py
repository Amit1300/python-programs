import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="manutd")
cur=myconn.cursor()
q="INSERT INTO players VALUES(%s,%s)"
val=[('martial',5),('martial',9),('martial',8),('martial',5),('martial',5),('martial',5)]
cur.executemany(q,val)
myconn.commit()
print(cur.rowcount)





