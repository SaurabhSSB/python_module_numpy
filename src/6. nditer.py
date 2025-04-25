import numpy as np
arr_1= np.arange(18).reshape(3,6)
print(arr_1)
for row in arr_1:
    print(row)
for row in arr_1:
    for cell in row:
        print(cell)
for cell in arr_1.flatten():
    print(cell)

for u in np.nditer(arr_1, order= "C"):
    print(u)
for v in np.nditer(arr_1, order= "F"):
    print(v)
for w in np.nditer(arr_1, order= "F", flags= ["external_loop"]):
    print(w)
for x in np.nditer(arr_1, op_flags= ["readwrite"]):
    x[...]= x*x

print(arr_1)
z= np.array(np.nditer(arr_1, flags= ["external_loop"], order= "F"))
print(z)

arr_2= np.arange(3).reshape(3,1)
print(arr_2)

for x, y in np.nditer([ arr_2, arr_1]):
    print( x, y)