import os

path = os.getcwd()
print(path)

# path = os.chdir("../")
# print(os.getcwd())

# os.path.join(parent, dir)
# os.remove()
# os.rmdir()
# os.mkdir()
# os.close()
# os.popen()

fd = "test.txt"
file = open("test.txt", "w")
file.write("hello")
file.close()

