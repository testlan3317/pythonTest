# Reading an Entire File:

with open('C:\\Users\\Jerome\\Documents\\Python3.9\\PythonFiles\\OOB\\Files\\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# becasue using vscode, there is a workplace concept here. 
# put 'pi_digits.txt' under the working place directory, then it will found the file. 
# in this case is C:\Users\Jerome\Documents\Python3.9\PythonFiles\
    
# or you can put the 'pi_digits.txt' under the same folder 
# in this case C:\\Users\\Jerome\\Documents\\Python3.9\\PythonFiles\\OOB\\Files\\pi_digits.txt
# be careful with the escape.


"""
Notice: how we call open() in this program but not close(). You could open and close the file by calling open() and close(),
but if a bug in your program prevents the close() method from being executed, the file may never close. 

This may seem trivial, but improperly closed files can cause data to be lost or corrupted. And if you call close() too early
in your program, you'll find yourself trying to work with a closed file (a file you can't access), which leads to more errors.
It's not always easy to know exactly when you should close a file, but with the structure shown here, Python will figure
that out for you.

All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when the
"with" block finished execution.

"""


# reading Line by Line
print("#########Reading Line by Line###################")
filename = "C:\\Users\\Jerome\\Documents\\Python3.9\\PythonFiles\\OOB\\Files\\pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#p258