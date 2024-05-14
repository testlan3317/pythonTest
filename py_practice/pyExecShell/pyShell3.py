# The final approach is - Subprocess
# The main function you want to keep in mind if you use Python>=3.5 is subprocess.run(), 
# subprocess module
# The subprocess.Popen() class : is reponsible for the creation and management of the executed process. 
# In contrast to the previous functions, this class executes only a single command with arguments as a list. 
# This means that you won't be able to "pipe" commands.

import subprocess
process = subprocess.Popen(['echo', 'More output'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

stdout,stderr = process.communicate()
print(stdout,stderr)
print(stdout.decode('utf-8'))
print(type(stdout.decode('utf-8')))

# you'll notice that we set "stdout" and "stderr" to subprocess.PIPE.
# This is special value that indicates to subprocess.Popen that a pipe should be opened that you can use ".communicate()" function.

"""
It's also possible to use a file object 

with open('text.txt','w') as f:
    process = subprocess.Popen(['ls','-l'], stdout=f)

Another thing, that you could notice is the output type is 'bytes'. you can resolve then by typing stdout.decode('utf-8')

or by adding "universal_newlines=True" when calling subprocess.Popen


"""
