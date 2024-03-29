# Queue

import threading
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [4, 5, 6], [6, 6, 6], [5, 4, 3]]
    results = []
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    for _ in range(4):
        results.append(q.get())
    print(results)


if __name__ == "__main__":
    multithreading()
