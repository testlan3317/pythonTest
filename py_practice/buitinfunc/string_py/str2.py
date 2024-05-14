# startsWith() - Return True or False
# txt.startswith(value, start, end)
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")
print(x)


# endsWith() - Return True or False
# txt.endswith(value, start, end)
#
x = txt.endswith(".")
print(x)


# find() - return the index
# finds the 1st occurrence of the specified value.
# txt.find(value, start, end) returns -1 if the value is not found
# find() is almost the same as index(), the only difference is that the index() method raises an exception if the value is not found
x = txt.find("welcome")
print(x)

# index()
# txt.index(value, start, end)
x = txt.index("welcome")
print(x)

print("================================")
# format()
# formats the specified values and insert them inside the string's placeholder
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

# isdigit()
# returns True if all the characters are digits, otherwise False
txt = "50900"
x = txt.isdigit()
print(x)

# isalnum()
# returns True if all the characters are alphanumeric, meaning alphabet lettter(a-z) and numbers(0-9)
txt = "Company12"
x = txt.isalnum()
print(x)

# islower()
# returns True if all characters are in lower case.
txt = "hello world"
x = txt.islower()
print(x)

# isnumeric()
# returns True if all the characters are numeric (0-9), otherwise False
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
txt = "565543"
x = txt.isnumeric()
print(x)

# isalpha()
# returns True if all the characters are alphabet letters(a-z)
txt = "CompanyX"
x = txt.isalpha()
print(x)

# isprintable()
# return True if all the characters are printable

# isspace(): Returns True if all characters in the string are whitespace
# txt.ispace()


print("==================================")
# issuper()

# islower()

# istitle()
# return True if all words in a text start with a upper case letter, and the reset of the word are lower case lettes.

print("===================================")
# partition()
# this method searches for the specified value, and splits the string into the "tuple" containing 3 elements.
# txt.partition(value)
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

# replace()
# txt.replace(oldvalue, newvalue, count)
# count - Optional, a number specifying how many occurrences of the old value you want to replace. Default is all occurrences
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# maketrans()
# txt.maketrans(x,y,z)
# x - source
# y - replacment
# z - which characters to remove from the original string
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))
print("===================================")

# strip()
# removes any leanding and trailling characters
# txt.strip(characters)
# character - optional. A set of characters to remove as leading/trailing characters
txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

# split()
# txt.split(separator, maxsplit)
# separator - Optional. Default is whitespace
# maxsplit - Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)
txt = "apple#bananas#cheery#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements
x = txt.split("#", 1)
print(x)

# zfill()
# txt.zfill(len)
# add zeros(0) at the beginning of the string, until it reaches the specified length.
txt = "50"
x = txt.zfill(10)
print(x)
