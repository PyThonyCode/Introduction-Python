import numpy as np

# INTRODUCTION
"""arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array((1, 2, 3, 4, 5))
print(type(arr1))
print(type(arr2))"""

# DIMENSIONS ARRAYS
# 0D
"""arr = np.array(30)
print(type(arr))"""
# 1D
"""arr = np.array([3, 1, 2, 4, 3])
print(arr)"""
# 2D
"""arr = np.array([[3, 1, 2, 4, 3], [3, 2, 3, 1, 9]])
print(type(arr))"""
# 3D
"""arr = np.array([[3, 2, 1], [3, 2, 2], [3, 9, 3]])
print(arr)"""
# 3D with 2D
"""arr = np.array([[[3, 3, 1], [6, 6, 2]], [[3, 2, 2], [6, 7, 8]]])
print(arr)"""

"""arr = np.array([3, 2, 6, 7, 8])
suma = arr[0] + arr[2]
print(f"La suma es : {suma}")"""

"""arr = np.array([[3, 2, 1], [6, 7, 9]])
suma = arr[1, 0] + arr[0, -1]
print(f"La suma es : {suma}")"""

"""arr = np.array([[[2, 4, 8], [9, 4, 3]], [[4, 2, 9], [0, 6, 1]]])
suma = arr[0, 1, 2] + arr[1, 1, 0]
print(f"La syma es : {suma}")"""

"""
arr = np.array([3, 4, 6, 8, 1, 22, 10])
print(arr[1:6:2])

arr = np.array([[3, 2, 1, 10, 3], [6, 7, 22, 11, 9]])
print(arr[1, :3])
print(arr[0:2, 2])

arr = np.array([3.2, 4.1, 6.7])
print(arr.dtype)
"""
"""arr = np.array([1, 2, 3, 4], dtype='f')
print(arr)
print(arr.dtype)"""

"""arr = np.array([3, 4, 5, 6, 12, 15, 22])
x = arr.copy()
arr[0] = 22
print(arr)
print(x)"""

"""arr = np.array([[3, 4, 5, 6], [8, 9, 6, 2]])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

print(arr.shape)"""

"""arr = np.array([3, 2, 6, 7, 8, 2, 1, 7])"""
# print(arr.reshape(2, 4))
"""for x in arr:
    print(x)

arr = np.array([[3, 2, 1], [4, 6, 8]])
for x in arr:
    print(x)

for x in arr:
    for y in x:
        print(y)

a = np.array([3, 2, 5])
b = np.array([7, 2, 1])
arr = np.concatenate((a, b))
print(arr)

a = np.array([[3, 2, 1], [6, 3, 6]])
b = np.array(([9, 7, 3], [1, 10, 2]))
arr = np.concatenate((a, b), axis=1)
print(arr)

arr = np.array([3, 1, 5, 7, 8, 22, 11, 0])
new_arr = np.array_split(arr, 5)
print(new_arr)

search = np.where(arr % 2 == 0)
print(search)
index = np.searchsorted(arr, 5)
print(type(index))"""

arr = np.array([3, 11, 2, 9, 33, 7])
print(np.sort(arr))

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is completely divisble by 2, set the value to True, otherwise False
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
