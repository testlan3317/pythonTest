# open(filename, "w"), create file and overwrite
f = open("demofiles1.txt", "w")
f.write("Woops! I have just create a new!")
f.close()

f = open("demofiles1.txt", "r")
print(f.read())

# try to create a new file call demofiles1.txt, if exists, create error
f = open("demofiles1.txt", "x")
