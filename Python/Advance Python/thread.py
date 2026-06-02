import threading
from time import sleep

def text_file():
    with open (r"C:\Users\Om\Desktop\SQL\Nested Subquery.txt") as file:
        for line in file:
            print(line)
            sleep(1)

def txt_file():
    with open (r"C:\Users\Om\Desktop\SQL\Select clause.txt") as file:
        for line in file:
            print(line)
            sleep(1)

thread1=threading.Thread(target=text_file)
thread2=threading.Thread(target=txt_file)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
