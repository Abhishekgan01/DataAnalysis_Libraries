import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).count_nonzero())

arr = np.array([[0, 2, 3], [4, 5, 6]])
print(csr_matrix(arr))

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
mat = csr_matrix(arr)
print("mat \n",mat)

print("sum of duplicate ",mat.sum_duplicates())
print("mat eliminate 0 \n",mat.eliminate_zeros())
print("mat \n",mat)


arr = np.array([[1, 0, 0], [0, 2, 1], [1, 0, 2]])

mtx = csr_matrix(arr)

#mtx.eliminate_zeros()
mtx.sum_duplicates()

print("mtx \n ",mtx)