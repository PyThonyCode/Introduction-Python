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

arr = np.array([3, 4, 6, 8, 1, 22, 10])
print(arr[1:6:2])

arr = np.array([[3, 2, 1, 10, 3], [6, 7, 22, 11, 9]])
print(arr[1, :3])
print(arr[0:2, 2])
