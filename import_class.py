
from matplotlib.pyplot import flag
from class_function import Timer


x = Timer()
print(x)
list_from_x = print(x.return_list())


liste = [1,2,3,4]

answer = all(x != 0 for x in liste)
print(answer)



import MySQLdb

mydb = MySQLdb.connect(host="lx31.hoststar.hosting",user="ch74838_web123",password="2013Pavoni!",db="ch74838_usr_web123_1")

#  you execute all the queries you need

cursor=mydb.cursor()
cursor.execute("SELECT CURDATE();")

# Use all the SQL you like
m = cursor.fetchone()
print("Today's Date Is ",m[0])
mydb.close()

