from win10toast import ToastNotifier
import time
import random
toaster = ToastNotifier()

with open('myquoteslist.txt') as fp:
    data = fp.readlines()

while(True):
    toaster.show_toast("Hey",
                       random.choice(data),
                       #icon_path="custom.ico",
                       duration=5)
    time.sleep(20)
