f = open("demofile3.txt", "a")
f.writelines(["See you soon!\n", "Over and out."])
f.close()

# open and read the file after the appending
f = open("demofile3.txt","r")
print(f.read())
