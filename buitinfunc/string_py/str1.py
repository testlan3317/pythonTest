# capitalize: uppercase the first letter
# txt.capitalize()

txt = "hello, and welcome to python study"

x = txt.capitalize()

print(x)

# txt.casefold(): make the string lower case
# similar to lower(), but stronger function

txt1 = "Hello, And Welcome To My World"

x1 = txt1.casefold()

print(x1)

# center()
# will center align the string, using a specified character (space is default) as the fill character.
# txt.center(length, character)

txt2 = "banana"
x2 = txt2.center(20, "!")
print(x2)


# count()
# return the number of times the value matches
# txt.count(value, start, end)
# start - Optional, The position to start the search. Default 0
# end - Optional, The position to end the search. Default is the end of the string
txt3 = "I love apples, apple are my favoirte fruit"
x3 = txt3.count("apple")
print(x3)

# encode(): returns an encoded version of the string

# expandtabs()
# sets the tab size
txt4 = "H\te\tl\tl\to"
x4 = txt4.expandtabs(2)
print(x4)
