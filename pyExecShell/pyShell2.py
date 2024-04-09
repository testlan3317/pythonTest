# os.popen(): --- This is useful since you can get the output as a variable
# This opens a pipe from or to the command line. 
# This means that we can access the stream within Python. 

import os
stream = os.popen('echo Returned output')
output = stream.read()
print(output)

# when you use the .read(), you'll get the whole output as one string.
# when you use .readlines() function, which splits each line (including a trailing \n)


stream1 = os.popen('echo Returned output \n \
        echo hello>hello.txt \n \
        cat hello.txt|grep he \n')
output1=stream1.readlines()
print(output1)
