# yield
# The yield statement suspends a function's execution and sends a value back to the caller, but retains enough state to enable the function
# to resume where it left off. 

# when the function resumes, it continues execution immediatly after the last yield run. 

# example
# a generator function that yields 1 for the first time, 2 second time and 3 third time

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


"""
1. yield is as return, but different
2. return sends a specified value back to its caller.
3. yield can produce a sequence of values(in the example, yield 1/2/3.
4. we should use yield when we want to iterator over a sequence, but don't want to store the entire sequence in memory.
"""

# yield for more understanding, see next example-> yield2.py
