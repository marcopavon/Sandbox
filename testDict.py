import csv
from fileinput import filename


test = {"Audi":{"color":"black","year":2000},
        "BMW":{"color":"white","year":1998},
        "Skoda":{"color":"white","year":1998},
        "Skoda2":{"color": ["blue","yellow"],"year":1998},
}

testList = ["Mercedes-Benz","Audi","BMW"]

def more(x):
        print(x)


def add2csv(fileName,data):
        with open(fileName,'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)


class Cars:
        def adapt_list(self,input):
                new_list = []
                for x in input:
                        new_list.append(x+" changed")
                return new_list

        def upper_case(self,list):
                for entry in self.adapt_list(list):
                        print(entry.upper())
        
        def printer(self,x):
                print(x)

        


x = Cars()
new_cars = x.adapt_list(testList)
x.printer(new_cars) 
 
x.upper_case(testList)