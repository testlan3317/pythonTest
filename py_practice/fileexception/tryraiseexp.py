# raise an exception
# Exception()

x = -1
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except:
    print("===Testing raising exception===")

finally:
    y = "hello"
    if not type(y) is int:
        raise TypeError("Only integers are allowed")
