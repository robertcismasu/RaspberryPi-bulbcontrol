import datetime
from time import sleep

class DateTime:
    def date_time():
        while(True):
            sleep(1)
            date_time = datetime.datetime.now()
            print ("Current date and time : ")
            print (date_time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    DateTime.date_time()