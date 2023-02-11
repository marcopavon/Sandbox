from cgi import test
from json.tool import main
import re
import sqlite3


from numpy import insert, tri

class sample:

    test = "test"
    def __init__(self):
        self.liste = [0,1,3,"a","b"]
        self.fk = "007"
        self.connection = sqlite3.connect("gfg.db")
        self.crsr = self.connection.cursor()
        
  
    
    def __str__(self):
        return str(self.liste)

    def __dir__(self):
        return str(self.liste), self.fk
    
    def clean (self):
        str_liste = str(self.liste)
        x = re.findall('[0-9]+', str_liste)
        for element in x:
            print(element)

    def out (self,x):
        print(x+self.fk)


    def create(self): 

        sql_command_emp = """CREATE TABLE IF NOT EXISTS emp (
        staff_number INTEGER PRIMARY KEY AUTOINCREMENT,
        fname VARCHAR(20),
        lname VARCHAR(30),
        gender CHAR(1),
        joining DATE);"""
        
        # execute the statement
        self.crsr.execute(sql_command_emp)
        
        
        # SQL command to create a table in the database
        sql_command_brother = """CREATE TABLE IF NOT EXISTS brother (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        fname VARCHAR(20),
        staff_id INTEGER,
        FOREIGN KEY (staff_id) REFERENCES emp(staff_number) ON DELETE CASCADE
        );"""
        
        # execute the statement
        self.crsr.execute(sql_command_brother)


    def insert(self, fname, lname, gender, date = "1980-10-29"):

        # another SQL command to insert the data in the table
        sql_command = """INSERT INTO emp (fname, lname, gender, joining) VALUES (?,?,?,?);"""
        sql_command_check = """SELECT * FROM emp where fname = ? AND lname = ? AND gender = ? AND joining = ?;"""
        
        check = self.crsr.execute(sql_command_check, (fname,lname, gender,date)).fetchone()
        print(check)

        if check is None:
            self.crsr.execute(sql_command, (fname,lname, gender,date))
        else:
            print('Entry exists')


    def check(self,fname,staffid):
           
        sql_command_check = """SELECT * FROM brother where fname = ? and staff_id = ?;"""
        check = self.crsr.execute(sql_command_check, (fname,staffid)).fetchone()
        
        if check is None:
            print(f"check-method: {fname} with staff_id:{staffid} not exists")
            return fname,staffid
        else:
            print(f'{fname} with staff_id:{staffid} exists')
            return None
            
    
    def insert_fk(self, fname, staff_id):
        # connecting to the database
        #connection = sqlite3.connect("gfg.db")
        self.connection('PRAGMA foreign_keys = ON;')
     
        # another SQL command to insert the data in the table
        sql_command = """INSERT INTO brother (fname, staff_id) VALUES (?,?);"""
        try:
            print(f"TRY: {fname}, {staff_id}")
            self.crsr.execute(sql_command, (self.check(fname,staff_id)))
            print(f"Out: {fname}, {staff_id}")
        except:
            print(f"no insert for {fname}, {staff_id}")
        

    def drop(self):

        # another SQL command to insert the data in the table
        sql_command = """
        DROP TABLE brother"""
        self.crsr.execute(sql_command)


    def update(self,fname,id):
                
        # another SQL command to insert the data in the table
        sql_command = """
        UPDATE emp set fname = ? where staff_number = ?
        """
        self.crsr.execute(sql_command, (fname,id))



    def delete(self,id):
            

            # another SQL command to insert the data in the table
            sql_command = """
            DELETE FROM emp where staff_number = ?
            """

            # Use  (id,)) with space, if you only have 1 parameter
            self.crsr.execute(sql_command, (id,))

    def delete_brother(self,id):
            

            # another SQL command to insert the data in the table
            sql_command = """
            DELETE FROM brother where staff_id = ?
            """

            # Use  (id,)) with space, if you only have 1 parameter
            self.crsr.execute(sql_command, (id,))

    def commit(self):
        self.connection.commit()

    def close (self):
        self.connection.close()


obj = sample()

obj.drop()
obj.create()
obj.insert("Tom","Cruise","M")
obj.insert("Tom","Jerry","M")
obj.insert("Tony","Hawk","M")
obj.insert("Milly","Cyrus","W") 
obj.insert("Clauda","Staub","W") 
obj.insert("Chris","Beneton","M") 

obj.insert_fk("cartoon","1")
obj.insert_fk("actor","9")
obj.insert_fk("Animal","24")

""" obj.check("VIP",1)
obj.check("Animal",10)
obj.check("Chief of Staff",99) """

#obj.update("Albert", 9)
#obj.delete(23)
#obj.delete_brother(23)

obj.commit()
obj.close()




'''
try:
    obj.insert("Tom","Cruise","M")
except:
    print("error raised")
    '''

""" if __name__ == '__main__':
    main() """