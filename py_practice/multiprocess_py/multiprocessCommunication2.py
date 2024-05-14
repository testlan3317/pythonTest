# Sharing data between processes
# 1. shared memory: multiprocessing module provides "Array" and "Value" objects to share data between processes.
# - Array: a ctypes array allocated from shared memory.
# - Value: a ctypes object allocated from shared memory.

import multiprocessing

def square_list(mylist, result, square_sum):
    """
    function to square a given list
    """
    # append squares of mylist to result array
    for idx, num in enumerate(mylist):  # enumerate: get a counter and the value from the iterable at the same time.
        result[idx] = num * num

    # square_sum value
    square_sum.value = sum(result)

    # print result Array
    print("Result(in process p1): {}".format(result[:]))

    # print square_sum Value
    print("Sum of squares(in process p1): {}".format(square_sum.value))


if __name__ == "__main__":
    # input list
    mylist = [1,2,3,4]

    # creating Array of int data type with space for 4 integers
    result = multiprocessing.Array('i', 4)  # i stands for integer whereas d stands for float data type
    print(f"result: {result}")
    # creating value of int data type
    square_sum = multiprocessing.Value('i') # i for data type, we could also add an initial value e.g. multiprocessing.Value('i', 10)
    print(f"square sum: {square_sum}")
    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

    # starting process
    p1.start()

    # wait until the process is finished
    p1.join()

    # print result array
    print("Result(in main program): {}".format(result[:]))  # result[:] print the complete array

    # print square_sum Value
    print("Sum of squares(in main program): {}".format(square_sum.value))

# Note: Array and Value are uppercase. And they are in shared memory(global)

