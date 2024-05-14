# use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

# Numpy does not change the data type of the element in-place( where the element is in array). so
# it needs some other space to perform this action. the extra space is called buffer.
# , and in order to enable it in nditer(), we pass flags=['buffered']

import numpy as np

arr = np.array([1,2,3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
