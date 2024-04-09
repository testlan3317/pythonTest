# Multiprocessing refers to the ability of a system to support more than one processor at the same time.
# Applications in a multiprocessing system are broken to smaller routines that run independently. 
# The operating system allocates these threads to the processors improving performance to the system.

# A multiprocessing system can have:
# multiprocessor: i.e. a computer with more than one central processor.
# multi-core processor: i.e. a single computing component with two or more independent actual processing units (called "cores")

# importing the multiprocessing module
import multiprocessing

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))

def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    # creating processes
    # args=() : tuple
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))
    
    # target: the function to be executed by process
    # args: the arguments to be passed to the target function
    # Note: Process constructor takes many other arguments.

    # starting process 1
    p1.start()

    # starting process 2
    p2.start()

    # wait until process 1 is finished 
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")



