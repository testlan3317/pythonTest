# This example gives the explanation of above mentioned note. Here, notice that the destructor is called after 
# the "Program End..." printed.

class Employee:

    def __init__(self):
        print('Employee created')


    def __del__(self):
        print("Destructor called")


def create_obj():
    print('making object ...')
    obj = Employee()
    print('function end...')
    return obj

print('calling create_obj() function ...')
obj = create_obj()
print('program end ...')
