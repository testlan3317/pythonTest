fruits = ["apple", "bananas", "cherry", "orange"]

fruits.clear()

print(fruits)

# clear()
# removes all the elements from a list

# insert()
# inserts the specified value at the specified position
fruits = ["apple", "bananas", "cherry"]
fruits.insert(1, "orange")
print(fruits)

# pop(): removes the elements at the specified position

fruits.pop(2)
print(fruits)

# remove(): removes the first item with the specified value

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# reverse() : reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()  # it will return None, so you can't print directly
print(fruits)

# sort()  :  sorts the list

fruits = ["pipeapple", "apple", "celery"]
fruits.sort()
print(fruits)


# count() methods returns the number of elements with the specified value
# return the number of times the value "cherry" appear in the fruits list.
fruits = ['apple', 'banana', 'cherry']
x = fruits.count('cherry')

print(x)

# extend()
# extend() the list elements or list or any iterable to the end of the current list. 
# list.extend(iterable)
# iterable - Required. Any iterable ( list, set, tuple, etc)
cars = ["Ford", "BMW", "volvo"]
points = (1, 4, 5, 8)
cars.extend(points)
print(cars)
