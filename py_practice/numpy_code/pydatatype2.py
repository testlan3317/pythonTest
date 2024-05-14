# copy vs view
# only view has the base. because it affected the original data. copy is a new data

import numpy as np

arr = np.array([1,2,3,4,5])

x = arr.copy()

y = arr.view()

print(x.base)
print(y.base)
