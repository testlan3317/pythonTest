# check if a Function is a ufunc
# A ufunc should return <class 'numpy.ufunc'>

import numpy as np

print(type(np.add))

print(type(np.concatenate))

# if the function is not recognized at all, it will return an error
