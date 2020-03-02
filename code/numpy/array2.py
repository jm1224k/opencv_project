import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([1, 2, 3], dtype=complex, ndmin=3)
arr3 = np.array(arr1, copy=False)
arr4 = np.array(np.mat('1 2; 3 4'), subok=True)

arr1[0] = [4, 5, 6]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
