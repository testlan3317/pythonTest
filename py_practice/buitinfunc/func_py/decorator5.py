# another example where we can find out the execution time of a function using a decorator

import time
import math

def calculate_time(func):

    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in: ", func.__name__, end - begin)
    return inner1

# this can be added to any function present.
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time so that you can see the actual difference.
    time.sleep(2)
    print(math.factorial(num))

# calling the function
factorial(10)
