# multiprocessing module provides a "Lock" class to deal with race conditions.
# "Lock" is implemented using a "Semaphore" object provided by the operating system.

"""
A semaphore is a synchronization object that controls access by multiple processes to a common resouce in a 
parallel programming environment.

It's simply a value in a designated place in operating system (or kernel) storage which each process can check
and then change.

Depending on the value that is found, the process can use the resource or will find that is already in use and must wait
for some period before trying again.

Semaphores can be binary (0 or 1) or can have conditional values. Typically, a process using semaphores checks the value and then, 
if  it using the resouces, it changes the value to reflect this so that subsequent semaphore users will know to wait.

"""

# next example: Pooling between processes

# Python program to illustrate the concept to locks in multiprocessing
import multiprocessing

# function to withdraw from account
def withdraw(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value -1
        lock.release()

# function to deposit to account
def deposit(balance, lock):
    for _ in range(10000):
        lock.acquire()     # lock.acquire(): apply lock
        balance.value = balance.value + 1
        lock.release()    # lock.release() : release lock

def perform_transactions():
    # initial balance (in shared memory)
    balance = multiprocessing.Value('i', 100)

    # creating a lock object
    lock = multiprocessing.Lock()  # Lock object is created

    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance, lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance, lock))

    # starting processes
    p1.start()
    p2.start()

    # wait until processes are finished
    p1.join()
    p2.join()

    # print final balance
    print("Final balance = {}".format(balance.value))
    


if __name__ == "__main__":
    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions()


