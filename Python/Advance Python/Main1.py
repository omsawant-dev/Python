import sqlite3
conn=sqlite3.connect("my_database.db")
cur=conn.cursor()

cur.execute('''CREATE TABLE EMP(ID INT PRIMARY KEY , ENAME TEXT,AGE INT,SALARY INT)''')
cur.execute('''INSERT INTO EMP VALUES(101,'VIRAT',35,300000),(102,'DDP',27,100000),(103,'PATIDAR',30,200000)''')
emp_data=cur.execute('''SELECT * FROM EMP''')
for emp in emp_data:
    print(emp)
print(list(emp_data))
print(emp_data.fetchall())
print(emp_data.fetchone())
conn.commit()
conn.close()
