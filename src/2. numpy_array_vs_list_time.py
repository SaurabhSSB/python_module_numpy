import numpy as np
import time
import sys

size= 1000000

list_1= range(size)
list_2= range(size)

array_1= np.arange(size)
array_2= np.arange(size)

# python list
start_list= time.time()
operation_list= [(x+y) for x,y in zip( list_1, list_2)]
print(f"Time taken by python list is {(time.time() - start_list) * 1000000}")

# numpy array
start_array= time.time()
operation_array= array_1 + array_2
print(f"Time taken by numpy array is {(time.time()- start_array) * 1000000}")