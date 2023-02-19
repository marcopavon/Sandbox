
from matplotlib.pyplot import flag
from class_function import Timer


x = Timer()
print(x)
list_from_x = print(x.return_list())


liste = [1,2,3,4]

answer = all(x != 0 for x in liste)
print(answer)

y=0
x= 0
print("test the loop")

while x <5:
    print(f"x= {x}")
    while x< 5 and y <5:
        print(f"x= {x} y= {y}")
        y+=1
    y=0
    x+=1
print("end the loop")

from selenium import webdriver

PROXY = "96.70.52.227:48324" #  HOST:PORT



import mysql.connector

cnx = mysql.connector.connect(user='ch74838_marco', password='Maverick-8',
                              host='lx31.hoststar.hosting',
                              database='ch74838_usr_web123_1')

c=cnx.cursor()
c.execute("""SELECT * FROM wp_users""")
sql_data = c.fetchall()
#print(c.fetchall())
print(sql_data)
cnx.close()

for data in sql_data:
    print("#########")
    print(data[1])



"""""
import MySQLdb

mydb = MySQLdb.connect(host="lx31.hoststar.hosting",user="ch74838_web123",password="2013Pavoni!",db="ch74838_usr_web123_1")

#  you execute all the queries you need

cursor=mydb.cursor()
cursor.execute("SELECT * wp_users")

# Use all the SQL you like
m = cursor.fetchone()
print(m)
mydb.close()

"""