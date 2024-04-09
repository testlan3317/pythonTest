# fromkeys(keys, value)
# keys - Required. An iterable specifying the keys of the new dictionary
# value - Optional. The value for all keys. Default value is None

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
