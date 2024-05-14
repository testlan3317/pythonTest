def f1():
    print("called f1")

def f2(f):  # pass f as parameter
    f()     # actually call f

f2(f1)   # pass f1 as parameter