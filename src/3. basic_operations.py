import numpy as np
arr_1d= np.array([1,2,3,4])
arr_2d= np.array([[ 1, 2, 3],[ 4, 5, 6]], dtype= np.float64)
arr_3d = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],

    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
], dtype= np.int32)

print(arr_1d)
print(arr_2d)

print(f"{arr_1d.ndim}d array")
print(f"{arr_2d.ndim}d array")

print(f"{arr_1d.itemsize} is the item size of 1d int64")
print(f"{arr_2d.itemsize} is the item size of 2d float64")

print(f"{arr_1d.dtype} is the data type of 1d array.")
print(f"{arr_2d.dtype} is the data type of 2d array.")

print(f"{arr_1d.size} is the size of 1d array.")
print(f"{arr_2d.size} is the size of 2d array.")

print(arr_3d)
print(f"{arr_3d.ndim}d array")
print(f"{arr_3d.itemsize} is the item size of 3d int32")
print(f"{arr_3d.dtype} is the data type of 3d array.")
print(f"{arr_3d.size} is the size of 3d array.")
print(f"{arr_3d.shape} is the shape of the 3d array.")

arr_3d_2= np.array([[[1,2,3]],[[4,5,6]]])
print(f"{arr_3d_2.ndim} is the dimension of 3d_2 array.")
print(f"{arr_3d_2.itemsize} is the item size of 3d_2 array.")
print(f"{arr_3d_2.dtype} is the data type of 3d_2 array.")
print(f"{arr_3d_2.size} is the shape of 3d_2 array.")
print(f"{arr_3d_2.shape} is the shape of 3d_2 array.")

arr_2d_2= np.array([[1,2],[3,4],[5,6]], dtype= complex)
print(arr_2d_2)

arr_zeros= np.zeros((5,6))
arr_ones= np.ones((2,3))
print(arr_zeros)
print(arr_ones)

arr_range= np.arange(5)
arr_range_2= np.arange( 5, 15, 2)

print(arr_range)
print(arr_range_2)

arr_linspace= np.linspace(1,12,5)
arr_linspace_2= np.linspace(1,6,6)
print(arr_linspace)
print(arr_linspace_2)

arr_3d_3= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_3d_3.shape)
arr_3d_3_2= arr_3d_3.reshape(12)
arr_3d_3_3= arr_3d_3.reshape(1, 1, 3, 4)
print(arr_3d_3_2)
print(arr_3d_3_3)

arr_3d_3_ravel= arr_3d_3.ravel()
print(arr_3d_3_ravel)