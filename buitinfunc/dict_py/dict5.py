car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

# items() returns a view object. 
# The view object contains the key-value pairs of the dictionary, as tuples in a list.


car['year'] = 2004

print(x)

# returns a view object contains the keys as a list.
x = car.keys()

print("keys",x)

# add price to the dict
car["price"]=12000

print(car)

# values(): returns a view object contains the values of dictionary

x = car.values()
print(x)

# pop(): removes the specified item from the dictionary.
car.pop("model")
print(car)

# popitem(): removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.

# setdefault()

x = car.setdefault("model", "Bronco")
print(x)

