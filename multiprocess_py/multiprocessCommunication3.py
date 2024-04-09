# server process: whenever a python program starts, a server process is also started. 
# From there on, whenever a new process is needed, the parent process connects to the server and requests it to fork a new process.

# A server process can hold Python objects and allows other processes to manipulate them using proxies. 

# multiprocessing module provides a "Manager" class which controls a server process.
# Hence, managers provide a way to create data that can be shared between different processes. 

"""
Pros and Cons:
1. Server process managers are more flexible than using "shared memory" objects because they can be made to support arbitrary
   object types like lists, dictionaries, Queue, Value, Array, etc. 
   Also, a single manager can be shared by processes on different computers over a network.

2. They are, however, slower than using shared memory.
"""

import multiprocessing

def print_records(records):
    """
    function to print record(tuples) in records(list)
    """
    for record in records:
        print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))

def insert_record(record, records):
    """
    function to add a new record to records(list)
    """
    records.append(record)
    print("New record added!\n")


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:         # with statement in your objects will ensure that you never leave any resource open.
        # creating a list in server process memory
        records = manager.list([('sam', 10), ('Adam', 9), ('Kevin', 9)])
        # new record to be inserted in records
        new_record = ('Jeff', 8)

        # creating new processes
        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        # running process p1 to insert new record
        p1.start()
        p1.join()

        # running process p2 to print records
        p2.start()
        p2.join()


# the manager is pretty much like a pool. 
