# get(keyname, value)
# returns the value of the item with the specified key
# value - optional, default return value if can't find it.

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}

x = car.get("model")

y = car.get("price", 15000)

print(x)

print(y)
