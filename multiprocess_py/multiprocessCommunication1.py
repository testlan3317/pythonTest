# multiprocess communication and data sharing
# in multiprocessing, any newly created process will do following
# 1. run independently 2. have their own memory space

import multiprocessing

# empty list with global scope
result = []

def square_list(mylist):
    """
    function to squre a given list
    """
    global result
    # append squares of mylist to global list result
    for num in mylist:
        result.append(num * num)
    # print global list result
    print("Result (in process p1): {}".format(result))


if __name__ == "__main__":
    # input list
    mylist = [1,2,3,4]

    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(mylist,))
    # starting process
    p1.start()
    # wait until process is finished
    p1.join()

    # print global result list
    print("Result(in main program): {}".format(result))

# After the completition of process p1 in the main program. Since main program is run by a different
# process, its memory space still contains the empty result list. 


