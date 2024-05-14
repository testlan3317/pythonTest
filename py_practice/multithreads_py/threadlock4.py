# Using Locks
# threading module provides a Lock class to deal with the race conditions. 
# Lock is implement using a Semaphore object provided by the OS. (details could check multiprocessing)

# Lock class provides following methods:
# 1. acquire() : lock
# 2. release() : release lock. if lock is already released, A ThreadError is raised.

import threading

# global variable x
x = 0

def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1

def thread_task(lock):
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        lock.acquire()   # apply lock
        increment()
        lock.release()

def main_task():
    global x
    # setting global variable x as 0
    x = 0

    # creating a lock
    lock = threading.Lock()

    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # start thread
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()

if __name__ == '__main__':
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x))

