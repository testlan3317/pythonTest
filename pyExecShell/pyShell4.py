# poll()
# we can use .poll() to check the return code of the process. It'll return "None" while the process is still running. 
# To get the output, you can use "process.stdout.readline()" - to read a single line
# To get multiple lines, use "process.stdout.readlines()"
# it reads all lines and it also waits for the process to finish if it has not finished yet. 

import subprocess

process = subprocess.Popen(['ping', '-c 4', 'python.org'],
                     stdout=subprocess.PIPE,
                     universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    # Do something
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # process has finished, read rest of the output
        for output in process.stdout.readlines():
            print(output.strip())
        print("Return code 1111")
        break
