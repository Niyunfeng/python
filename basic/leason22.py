# threading join

import threading
import time


def T1():
    print("T1 start. \n")
    time.sleep(1)
    print("T1 finish. \n")


def T2():
    print("T2 start. \n")
    print("T2 finish. \n")


t1 = threading.Thread(target=T1, name="T1")
t2 = threading.Thread(target=T2, name="T2")
t1.start()
t2.start()
t2.join()
t1.join()

print("all done.")
