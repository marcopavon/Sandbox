import time
import datetime


class Timer:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return "Test()"
    def __str__(self):
        return f"All we got is {self.current_time}"
    
    def return_list(self):
        return [self.current_time, "locker"]






