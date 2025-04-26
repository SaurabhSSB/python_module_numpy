import numpy as np

arr_1= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)
print(arr_1.min())
print(arr_1.max())
print(arr_1.sum())
print(arr_1.sum(axis= 0))
print(arr_1.sum(axis= 1))

arr_1_sqrt= np.sqrt(arr_1)
print(arr_1_sqrt)

arr_1_std= np.std(arr_1)
print(arr_1_std)


arr_2= np.array([[1,2],[3,4]])
arr_3= np.array([[5,6],[7,8]])

arr_4= arr_2 + arr_3
arr_5= arr_2 - arr_3
arr_6= arr_2 * arr_3
arr_7= arr_2 / arr_3
print(arr_4)
print(arr_5)
print(arr_6)
print(arr_7)

arr_8= arr_2.dot(arr_3)
print(arr_8)
