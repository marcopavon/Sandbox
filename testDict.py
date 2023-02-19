# importing datetime module
import datetime
  
# date in yyyy/mm/dd format
d1 = datetime.datetime(2018, 5, 3)
d2 = datetime.datetime(2018, 6, 1)

diction ={
        "name":"The Palazzo",
        "size": 120,
        "extras":{
                "pool":True,
                "bbq":False
        }
}

class Property:
        def __init__(self,**kwargs):
                for key, value in kwargs.items():
                        print(key, '-', value)
                        setattr(self, key, value)
                self.plot = list(["a",""])

        def create_list(self):
                output = list([self.name,self.size])
                return output

        def get_name(self):
                return self.name.upper()




class Customer:
        def __init__(self,name, year, house):
                self.name = name
                self.year = year
                self.house = house
        
        def __str__(self):
            return f"{self.name}, {str(self.year)}, {self.house}"


prop_palazzo = Property(**diction)
print(prop_palazzo.name)
print(prop_palazzo.plot)
print(prop_palazzo.get_name())
print(prop_palazzo.create_list())

prop_diamond = Property(name="diamong",size=134)
print(prop_diamond.create_list())

peter= Customer("Peter",2025,prop_diamond.name)

print(peter)

class Dynamic(Property):
        def __init__(self):
                self.static = False
                self.name = "oski"


new = Dynamic()

print(new.get_name())
