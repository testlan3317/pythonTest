# readlines()
# returns a list, containing each line in the file as a list item
# readlines(hint)
# hint - Optional. If the number of bytes returned execeed "hint", no more lines will be returned. Default is -1, means all lines return.

f = open("demofiles.txt", "r")
print(f.readlines(33))
