# string formatting
# txt.format(variable)
price = 49
txt = "The price is {} dollars"
txt1 = "The price is {:.2f} dollars - float"
print(txt.format(price))
print(txt1.format(price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "Hist name is {1}. {1} is {0} years old"
print(txt.format(age, name))


#name indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
