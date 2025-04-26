import numpy as np
arr_1= np.array([1,2,3])
print(arr_1[0:2])
print(arr_1[- 1])

arr_2= np.array([[1,2,3],[4,5,6]])
print(arr_2)
print(arr_2[1,2])

arr_3= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_3)
print(arr_3[0:2,2])
print(arr_3[-1,0:2])
print(arr_3[:,1:3])

for row in arr_3:
    print(row)

for cell in arr_3.flat:
    print(cell)

arr_4= np.arange(6).reshape(2,3)
arr_5= np.arange(6,15).reshape(3,3)
arr_6= np.arange(5,15).reshape(2,5)
print(arr_4)
print(arr_5)
print(arr_6)

arr_7= np.vstack(( arr_4, arr_5))
print(arr_7)

arr_8= np.hstack(( arr_4, arr_6))
print(arr_8)

arr_9= np.hsplit(arr_8,2)
print(arr_9)
print(arr_9[0])
print(arr_9[1])

arr_10= np.vsplit(arr_7,5)
print(arr_10)
print(arr_10[0])
print(arr_10[1])
print(arr_10[2])
print(arr_10[3])
print(arr_10[4])

arr_11= np.arange(12).reshape(3,4)
print(arr_11)

bool_comparison= arr_11 > 4
print(bool_comparison)
print(arr_11[bool_comparison])
arr_11[bool_comparison]= -16
print(arr_11)