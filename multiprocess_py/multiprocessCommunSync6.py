# synchronization
# - synchronization between processes
# - Pooling of processes

# process synchronization is defined as a mechanism which ensures that two or more concurrent processes do not 
# simultaneously execute some particular program segement known as "critical section".

# "Critical section" refers to the parts of the program where the shared resource is accessed.

"""
Concurrent accesses to shared resource can lead to race condition

A race condition occurs when two or more processes can access shared data and they try to change it at the same time.
As a result, the values of variables may be unpredictable and vary depending on the timings of context switches of 
the processes.

"""

# Lock and Semaphore - next example

import multiprocessing

# Python program to illustrate the concept of race condition in multiprocessing

# function to withdraw from account
def withdraw(balance):
    for _ in range(10000):
        balance.value = balance.value -1

# function to deposit to account
def deposit(balance):
    for _ in range(10000):
        balance.value = balance.value + 1

def perform_transactions():
    # initial balance (in shared memory)
    balance = multiprocessing.Value('i', 100)

    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance,))
    p2 = multiprocessing.Process(target=deposit, args=(balance,))

    # starting processes
    p1.start()
    p2.start()

    # wait until processes are finished
    p1.join()
    p2.join()

    # print final balance
    print("Final balance = {}".format(balance.value))


if __name__ == '__main__':
    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions()

