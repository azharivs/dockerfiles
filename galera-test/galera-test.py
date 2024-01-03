import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="172.17.0.2",
  user="vahid",
  password="vahid"
)

mycursor = mydb.cursor()

now = datetime.datetime.now()
sql = "INSERT INTO galeratest.test_table (msg) VALUES (%s)"
val = "{}: record added by PRIMARY u-serv".format(now)
mycursor.execute(sql, (val,))
mydb.commit()

mycursor.execute("SELECT * FROM galeratest.test_table;")
for x in mycursor:
  print(x)

mycursor.execute("show variables like 'wsrep_node_%';")
for x in mycursor:
  print(x)

mycursor.execute("show status like 'wsrep_cluster_%';")
for x in mycursor:
  print(x)

