import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])

print(arr.shape)

print(arr[1:3])
# [start:end:step]
print(arr[::2])
# 3rd row all and printing 2 steps apart from 2st row
print(arr[2:, 1::2])
