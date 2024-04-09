# fileno() returns the file descriptor of the stream, as a number
# an error will occur if the operator system does not use a file descriptor.

f = open("demofiles.txt", "r")
print(f.fileno())
