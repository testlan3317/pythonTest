# Iterator in Python is an object that is used to iterator over iterable objects like lists, tuples, dicts, and sets.

# The iterator object is initialized using the iter() method. It uses the next() method for iteration.

# 1. __iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
# 2. __next__(): The next() method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses
# the iter() method to get an iterator object, which further uses the next() method to iterator over. 


# creating iterator with iter()
string = 'gfg'
ch_iterator = iter(string)


print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
