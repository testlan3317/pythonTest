# why ufuncs?
# ufuncs are used to implement vectorization in Numpy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. That are very helpful for computation.

# ufuncs also take additional arguments, like:

# where - boolean array or condition defining where the operations should take place.
# dtype - defining the return type of elements
# out - ouput array where the return value should be copied.

import numpy as np

x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)

print(z)

# return [5 7 9 11]
