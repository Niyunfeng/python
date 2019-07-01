from time import *
from queue import Queue
import threading
from copy import *


def job(l, q):
    res = sum(l)
    q.put(res)


def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy(l), q), name="T%i" % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal(l):
    print(sum(l))


if __name__ == "__main__":
    l = list(range(1000000))
    st_ = time()
    normal(l * 4)
    print("running time:", time() - st_)
    st_ = time()
    multithreading(l)
    print("running time:", time() - st_)

