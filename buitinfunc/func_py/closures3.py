# Python program to illustrate closure

import logging
logging.basicConfig(filename="example.log", level=logging.INFO)

def logger(func):
    
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    
    return log_func

def add(x,y):
    return x+y

add_logger = logger(add)
add_logger(3, 3)
