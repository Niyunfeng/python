# threading

import threading
import time


def thread_job():
    print("This is a thread of %s \n" % threading.current_thread())

    # print all threading info
    print(threading.enumerate())

    # print active threading count
    print("in thread, active count is :", threading.activeCount())


def main():
    thread = threading.Thread(target=thread_job)
    thread.start()
    thread.join()
    # print active threading count
    print("in main ,active count is :", threading.activeCount())


if __name__ == "__main__":
    main()

# time.sleep(0.5)

