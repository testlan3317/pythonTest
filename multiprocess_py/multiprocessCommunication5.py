# Pipes: A pipe can have only two endpoints
# Hence, it is preferred over queue when only two-way communcation is required.

# multiprocessing module provides Pipe() function which returns a pair of connection objects connected by a pipe.
# The two connection objects return by Pipe() represent the two ends of the pipe.

# Each connection object has send() and recv() methods (among others)

import multiprocessing

def sender(conn, msgs):
    """
    function to send messages to other end of pipe
    """
    for msg in msgs:
        conn.send(msg)
        print("Sent the message: {}".format(msg))
    conn.close()


def receiver(conn):
    """
    function to print the messages received from other end of pipe
    """
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message: {}".format(msg))

if __name__ == '__main__':
    # message to be sent
    msgs = ["hello", "hey", "hru?", "END"]
    # creating a pipe
    parent_conn, child_conn = multiprocessing.Pipe()
    print(type(parent_conn))
    # Creating new processes
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn, ))

    # running processes
    p1.start()
    p2.start()

    # wait until processes finish
    p1.join()
    p2.join()
