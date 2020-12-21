import numba as nb
import numpy as np
from numba import prange


a = np.array([
    [0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
], dtype='b1')

Numba2dBooleanArray = nb.typeof(a)


print(a.dtype)
print(Numba2dBooleanArray)


@nb.njit(nb.uint32(Numba2dBooleanArray), fastmath=True)
def largest_cross(a):
    r, l = a.shape
    # optimize for memory usage by setting the type
    left = np.zeros(a.shape, dtype=nb.uint32)
    right = np.zeros(a.shape, dtype=nb.uint32)
    top = np.zeros(a.shape, dtype=nb.uint32)
    bottom = np.zeros(a.shape, dtype=nb.uint32)

    for i in range(r):
        for j in range(1, l):
            if a[i][j-1]:
                left[i][j] = left[i][j-1] + 1

    for i in range(r):
        for j in range(l-1, -1, -1):
            if a[i][j+1]:
                right[i][j] = right[i][j+1] + 1

    for j in range(l):
        for i in range(1, r):
            if a[i-1][j]:
                top[i][j] = top[i-1][j] + 1

    for j in range(l):
        for i in range(r-1, -1, -1):
            if a[i+1][j]:
                bottom[i][j] = bottom[i+1][j] + 1

    max_cross = 0
    for i in range(r):
        for j in range(l):
            cur = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
            max_cross = max(cur, max_cross)

    return max_cross


print(largest_cross(a))