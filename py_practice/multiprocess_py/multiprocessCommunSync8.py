# Pooling between processes

# in order to utilize all the cores, multiprocessing module provides a "Pool" class.
# The "Pool" class represents a pool of worker processes. 
# it has methods which allows tasks to be offloaded to the worker processes in a few different ways.


# python program to find square of numbers in a given list

import multiprocessing
import os

def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n*n)

if __name__ == '__main__':
    # input list
    mylist = [1,2,3,4,5]

    # creating a pool object
    p = multiprocessing.Pool()

    # map list to target function
    result = p.map(square, mylist)

    print(result)

# There are a few arguments for gaining more control over offloading of task. These are:
# 1. processes: specify the number of worker processes.
# 2. maxtasksperchild: specify the maximum number of task to be assigned per child.

# all the processes in a pool can be made to perform some initialization using these arguments:
# 1. initializer: specify an initialization function for worker processes
# 2. initargs: arguments to be passed to initializer


