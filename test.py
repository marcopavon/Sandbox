from dataclasses import fields
import datetime
import time
from typing import Counter
import csv

testDic = {"Audi":{"color":"black","year":2000},
        "BMW":{"color":"white","year":1998},
        "Skoda":{"color":"white","year":1998},
        "Skoda2":{"color": ["blue","yellow"],"year":1998},
}

class Dic:
    testDic = {"Audi":{"color":"black","year":2000},
        "BMW":{"color":"white","year":1998},
        "Skoda":{"color":"white","year":1998},
        "Skoda2":{"color": ["blue","yellow"],"year":1998},
}

def runs():
        
    print("hello")

    x = "ok"
    y = 2

    print(x+str(y))
    x = [22,33]
    for y in x:
        print(y)

    lov = {"y":"beute", "d":"bambus"}

    for x in lov:
        print(lov[x])
        print(x)



    folder = ["Mercedes-Benz","Audi","BMW"]
    if "Audi" in folder:
        print("audi in list")
    else:
        print("no audi - bug!")

    """ for element in folder:
        print("testDic with: "+ element)
        if "Audi" in element:
            print("its AUDI")
        elif "BMW" in element:
            print ("its BMw")
        else:
            print("something else") """


    for element in testDic:
        #print(testDic[element], element, element["color"])
        print(element, testDic[element]["color"])

    print(testDic)

    for data in testDic["Skoda2"]["color"]:
        print(data)


    aa = time.time()

    """ counter = 0
    from time import sleep
    while counter <5:
        sleep(1)
        print("still on")
        counter +=1
        # thing to rund
    """


    test ={}
    a = datetime.datetime.today()
    test["a"] = str(a)
    print(test)

    print("end script")

    idd ={}
    idd["productid=29"] = {}
    idd["productid=29"]["duration"] = "ELVIA not listed"
    idd["productid=29"]["date"] =2

    print(idd)
    fields =  [a]
    with open('test.csv','a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


    b = time.time()

    print(round(b-aa))

    test = datetime.datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
    test2= str(datetime.datetime.now().strftime("%Y-%m-%d - %H:%M"))
    print(test)
    print(test2)


    tst = {"a":1,"b":2}
    print(idd)
    low_key = min(tst, key=tst.get)
    print(low_key)


    dicto = {"alpha":{"item1":1, "item2":2,"more":{"sub1":"ok","sub2":"go"}}
    }

    kk = dicto["alpha"]["more"].get("sub1")
    print(kk)

    import re

    string = "akakdfkl0009**,99gg CHF 90'000.00"
    s = re.sub("[^CHF0-9\.]", "", string)
    ss= re.search("(.*)(CHF\W)(.*)", string)
    output = ss.group(3)
    sss = re.sub("'","",output)

    print(sss)

    ll=["AG","ZH","BE"]
    ll2=["a","b","c"]
    ll3=["1970","1980","1990"]

    def hello(kanton,typ,jahr):
        print(kanton, typ, jahr)

    for x in ll:
        for y in ll2:
            for z in ll3:
                hello(x,y,z)


    print(int(ll3[0])+10)

    #print(s)

    """ f1 = open("khh-prime.csv", "r")
    last_line = f1.readlines()[-800:]

    for line in last_line:
        if "no promo" not in line:
            print(line)
            print("yes") """


    """ f1 = open("delay.csv", "r")
    last_line = f1.readlines()[-3:]
    print(last_line)
    print(last_line[0])

    if  "not listed" in last_line[0] and "not listed" in last_line[1] and "not listed" in last_line[2]:
        print("ELVIA Issue")

    elif int(last_line[0].split(",")[-1]) >10 and int(last_line[1].split(",")[-1]) >10:
        print("Comparis Issue")
    else:
        print("All Good")
    f1.close() """