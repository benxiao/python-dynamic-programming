import numpy as np
import numba as nb


Nb_I64Array1d = nb.typeof(np.array([1], dtype=np.int64))
Nb_F64Array1d = nb.typeof(np.array([1], dtype=np.float64))


@nb.njit(nb.int64(Nb_I64Array1d, nb.int64), fastmath=True)
def bisect_right(a, x):
    lo, hi = 0, len(a)
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo


@nb.njit(Nb_I64Array1d(Nb_F64Array1d))
def convert_to_int(p):
    mi = p.min()
    p /= mi
    return p.astype(np.int64)


@nb.njit(Nb_I64Array1d(Nb_F64Array1d, nb.int64), parallel=True)
def random_choice_by_p_float(p, size):
    p = convert_to_int(p)
    p = np.cumsum(p)
    ma = p.max()
    x = np.random.randint(0, ma, size)
    result = np.zeros(size, dtype=np.int64)
    for i in nb.prange(size):
        result[i] = bisect_right(p, x[i])
    return result


if __name__ == '__main__':
    import time
    start = time.time()
    np.random.choice([0, 1, 2], 1000_000, p=[0.01, 0.01, 0.98])
    np_solution = time.time()-start
    print(f"np.random.choice = {np_solution:.6f}s")

    start = time.time()
    random_choice_by_p_float(np.array([1.0, 1.0, 1.0, 0.1, 3.0]), 1000_000)
    my_solution = time.time()-start
    print(f"random_choice_by_p_float = {time.time()-start:.6f}s")

    print(f"{np_solution / my_solution: .2f} x speed up")
