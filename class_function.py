import time
import datetime
import os
import sys


class Timer:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_time_miliseconds = datetime.datetime.now()

    def __repr__(self):
        return "Test()"
    def __str__(self):
        return f"All we got is {self.current_time}"
    
    def return_list(self):
        return [self.current_time, "locker", self.current_time_miliseconds]


class Csv:
    csv_file =  os.path.join(sys.path[0], "test_file.csv")

    def read_out(self):
        f1 = open(self.csv_file, "r")
        return f1.readlines()[-3:]

    def read_out_all(self):
        f1 = open(self.csv_file, "r")
        return f1.readlines()

    def clean_data(self, input):
        splitt_list = input.split(" ")
        return splitt_list[0]



    def read_out_element(self):
        for x in self.read_out():
            print(self.clean_data(x))


if __name__ == "__main__":
    new_file = Csv()
    new_file.read_out_element()

#print(f"This is the current directory, which you are in: {os.getcwd()}")
