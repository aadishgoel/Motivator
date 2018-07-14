from win10toast import ToastNotifier
import time
import random
from data import data
toaster = ToastNotifier()

while(True):
    quote = random.choice(data)
    toaster.show_toast(quote["author"],
                       quote["quote"],
                       duration=10)
    time.sleep(5)
