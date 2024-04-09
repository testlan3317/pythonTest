# There is a useful function from "shlex" module

# shlex.split("/bin/prog -i data.txt -o \"more data.txt\"")

import shlex


output = shlex.split("/bin/prog -i data.txt -o \"more data.txt\"")
print(type(output))
print(output)

output1 = shlex.split("cat controller.log|grep FGVM04TM22038193 > controller.log.1")
print(output1)


# subprocess.call() function : it works like Popen() class, but it waits until the command completes and gives you the return code as in
# return_code = subprocess.call(['echo', 'Even more output']).
# The recommended way however is to use "subprocess.run()" which works since Python3.5. It has been added a simplification of subprocess.Popen.
# the function will return a subprocess.CompletedProcess object:
"""
process = subprocess.run(['echo', 'Even more output'],
                    stdout=subprocess.PIPE,
                    universal_newlines=True)

print(process)

# similar to subprocess.call() and the previous .communicate() function, it will wait till the process is completed. 
"""
