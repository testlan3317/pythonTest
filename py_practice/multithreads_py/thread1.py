# Thread
# In computing, a process is an instance of computer program that is being executed. Any process has 3 basic components:
# 1. an executable program
# 2. the associated data needed by the program (variable, work space, buffers, etc.)
# 3. the execution context of the program (State of process)

# A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be
# performed in an OS. 
# In simple words, a thread is a sequence of such instructions within a program that can be executed independently of the other code.
# For simplicity, you can assume that thread is simply a subset of a process. 


# A thread contains all this information in a Thread Control BLock (TCB):
# - Thread Identifier: Unique id (TID) is assigned to every new thread
# - Program counter: a register which stores the address of the instruction currently being executed by thread.
# - stack pointer: Points to thread's stack in the process. Stack contains the local variables under thread's scope
# - Thread state: can be running, ready, waiting, start or done.
# - Thred's register set: registers assigned to thread for computations.
# - Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.


"""

Multi-threading: Multiple threads can exist within one process where:
    - Each thread contains its own register set and local variables (stored in stack)
    - All threads of a process share global variables (stored in heap) and the program code.

multithreading is defined as the ability of a processor to execute multiple threads concurrently.

In a simple, single-core CPU, it is achieved using frequent switching between threads. 
This is termed as "context switching"

In context switching, the state of a thread is saved and state of another thread is loaded whenever any interrupt (due to I/O
manually set) takes place. 

Context switching takes place so frequently that all the threads appear to be running paralley (this is termed as multitasking).

"""

# In python, the "threating" module provides a very simple and intuitive API for spawning multiple threads in a program.

import threading

def print_cube(num):
    # function to print cube of given num
    print("Cube: {}".format(num * num * num))

def print_square(num):
    # function to print square of given num
    print("Square: {}".format(num * num))


if __name__ == '__main__':
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
