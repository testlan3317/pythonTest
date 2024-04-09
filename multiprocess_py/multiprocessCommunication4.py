# Effective use of multiple processes usually requires some communication between them, 
# so that work can be divided and results can be aggregated.

# multiprocessing supports 2 types of communication channel between processes:
# 1. Queue
#
# Queue is a simple way to communicate between process with multiprocessing is to use a Queue to pass messages back and forth.
# Any Python can pass through a Queue
# Note: the multiprocessing.Queue class is near clone of queue.Queue.

# 2. Pipe (next py example)

import multiprocessing

def square_list(mylist, q):
    """
    function to square a given list
    """
    for num in mylist:
        q.put(num * num)

def print_queue(q):
    """
    function to print queue elements
    """
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")

if __name__ == '__main__':
    mylist = [1,2,3,4]

    # creating multiprocessing Queue
    q = multiprocessing.Queue()

    # creating new processes
    p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))

    # running process p1 to square list
    p1.start()
    p1.join()

    # running process p2 to get queue elements
    p2.start()
    p2.join()


