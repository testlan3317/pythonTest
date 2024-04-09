# The "contextlib" module provides a few more abstractions built upon the basic context manager interface.

from contextlib import contextmanager

class MessageWriter(object):
    def __int__(self, filename):
        self.file_name = filename

    @contextmanager
    def open_file(self): 
        # because of the "yield" statement in its definition, the function "open_file()" is a generator function.
        # when this open_file() function is called, it creates a resource descriptor named file.
        # This resource descriptor is then passed to the caller - here is "my_file".
        # After the code inside the with block is executed the program control returns back to the open_file() function.
        # The open_file() function resumes its execution and executes the code following the "yield" statement.
        try:
            file = open(self.file_name, 'w')
            yield file
        finally:
            file.close()

    # usage
    message_writer = MessageWriter('hello.txt')
    with message_writer.open_file() as my_file:
        my_file.write('hello world')


