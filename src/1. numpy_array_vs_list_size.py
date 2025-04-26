# Numpy
# fast, convenient, less memory

# Numpy Arrays:Numpy
# fast, convenient, less memory
import numpy as np
arr_1 = np.array([1, 2, 34, 35])
print(arr_1)
print(type(arr_1))
print(arr_1[1])

# Time and sys Modules:
import time
import sys

list_1 = range(1000)
print(sys.getsizeof(5) * len(list_1))

# Numpy Array Size and Itemsize:
import numpy as np

arr_2 = np.arange(1000)
print(arr_2.size * arr_2.itemsize)

