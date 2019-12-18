import numba as nb
from numba import njit
import numpy as np


NumbaBytesType = nb.typeof("".encode())


@njit(nb.int32(NumbaBytesType, NumbaBytesType))
def jit_edit_dist(b0: bytes, b1: bytes) -> nb.int32:
    m, n = len(b0), len(b1)
    cache = np.zeros((m + 1, n + 1))
    for i in range(m + 1):
        cache[i, 0] = i

    for j in range(n + 1):
        cache[0, j] = j

    for i, c0 in enumerate(b0):
        for j, c1 in enumerate(b1):
            if c0 == c1:
                cache[i + 1, j + 1] = cache[i, j]
            else:
                penalty = 2 if (i < 2 or j < 2) else 1
                cache[i + 1, j + 1] = penalty + min(
                    cache[i, j + 1],  # insert
                    cache[i + 1, j],  # delete
                    cache[i, j]  # replace
                )

                # adjacent character transportation
                if b0[i] == b1[j-1] and b0[i-1] == b1[j]:
                    cache[i+1, j+1] = min(
                        cache[i-1, i-1] + 1,
                        cache[i+1, j+1]
                    )

                # two repeats characters counts
                if i > 0 and j > 0 and b0[i] == b0[i-1] and b1[j] == b1[j-1]:
                    cache[i+1, j+1] = min(
                        cache[i-1, i-1] + 1,
                        cache[i+1, j+1]
                    )

    return cache[m, n]


@njit(nb.int32(NumbaBytesType, NumbaBytesType))
def jit_lsc(b0: bytes, b1: bytes) -> nb.int32:
    m, n = len(b0), len(b1)
    cache = np.zeros((m + 1, n + 1))
    for i, c0 in enumerate(b0):
        for j, c1 in enumerate(b1):
            if c0 == c1:
                cache[i + 1, j + 1] = cache[i, j] + 1
            else:
                cache[i + 1, j + 1] = max(
                    cache[i, j + 1],
                    cache[i + 1, j])
    return cache[m, n]


def fast_edit_distance(s0: str, s1: str, encoding='utf-8') -> int:
    return jit_edit_dist(s0.encode(encoding), s1.encode(encoding))


def fast_lsc(s0: str, s1: str, encoding='utf-8') -> int:
    return jit_lsc(s0.encode(encoding), s1.encode(encoding))


if __name__ == '__main__':
    print(fast_edit_distance("abbcd", "aggcd"))
    print(fast_lsc("tr l", "trs l"))
