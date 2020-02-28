import numpy as np

array = np.arange(12)

reshape1 = array.reshape(2, 3, 2)
reshape2 = np.reshape(array, (2, -1), order='F')
reshape3 = np.reshape(array, (2, -1), order='C')
reshape4 = np.reshape(array, (6, -1), order='F')

print(reshape1)
print(reshape2)
print(reshape3)
print(reshape4)
