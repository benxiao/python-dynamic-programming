import numpy as np
import numba as nb

a = [[2, 4, -2, 2],
     [4, 9, -3, 8],
     [-2, -3, 7, 10]]

b = [[1, 1, 1, 7], [1, 1, -1, 5], [1, -1, 1, 3]]


def ut_wrapper(a):
    a = np.array(a, dtype=np.float)
    return ut(a)


# back substitution
@nb.njit()
def bs(a):
    n_unknowns = a.shape[0]
    unknowns = np.empty((n_unknowns,))
    # bottom up
    for k in range(n_unknowns-1, -1, -1):
        t = a[k, n_unknowns]
        if k+1 < n_unknowns:
            t -= np.dot(a[k, k+1:n_unknowns], unknowns[k+1:])
        unknowns[k] = t / a[k][k]
    return unknowns


# upper triangular form
@nb.njit()
def ut(a):
    n_unknowns = a.shape[0]
    for i in range(n_unknowns - 1):
        # check pivot is not zero
        j = i + 1
        if a[i][i] == 0:
            while j < n_unknowns and a[j][i] == 0:
                j += 1

            if j == n_unknowns:
                print(a)
                raise ValueError("zero pivot")

            tmp = a[i].copy()
            a[i] = a[j]
            a[j] = tmp

        pivot = a[i][i]
        for k in range(i+1, n_unknowns):
            # if it already zero, skip
            if a[k][i] == 0:
                continue
            multiplier = a[k][i] / pivot
            a[k] -= (multiplier * a[i])

        # print(a)
    return a





if __name__ == '__main__':
    result = ut_wrapper(b)
    print(result)
    print(bs(result))
