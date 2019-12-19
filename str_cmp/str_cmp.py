import numba as nb
from numba import njit
import numpy as np

NumbaBytesType = nb.typeof("".encode())


@njit(nb.int32(NumbaBytesType, NumbaBytesType))
def jit_hamming_distance(b0: NumbaBytesType, b1: NumbaBytesType) -> nb.int32:
    dist = abs(len(b0) - len(b1))
    for c0, c1 in zip(b0, b1):
        if c0 != c1:
            dist += 1
    return dist


@njit(nb.int32(NumbaBytesType, NumbaBytesType))
def jit_edit_dist(b0: NumbaBytesType, b1: NumbaBytesType) -> nb.int32:
    m, n = len(b0), len(b1)
    cache = np.zeros((m + 1, n + 1))
    for i in range(1, m + 1):
        cache[i, 0] = cache[i - 1, 0] + (2 if i < 2 else 1)

    for j in range(1, n + 1):
        cache[0, j] = cache[0, j - 1] + (2 if j < 2 else 1)

    for i, c0 in enumerate(b0):
        for j, c1 in enumerate(b1):
            if c0 == c1:
                cache[i + 1, j + 1] = cache[i, j]
            else:
                penalty = 2 if (i < 2 and j < 2) else 1
                cache[i + 1, j + 1] = penalty + min(
                    cache[i, j + 1],  # insert
                    cache[i + 1, j],  # delete
                    cache[i, j]  # replace
                )
                # damerau levenshtein
                # adjacent character transportation
                if i > 2 and j > 2 and b0[i] == b1[j - 1] and b0[i - 1] == b1[j]:
                    cache[i + 1, j + 1] = min(
                        cache[i - 1, i - 1] + 1,
                        cache[i + 1, j + 1]
                    )

                # two repeats characters counts
                if i > 0 and j > 0 and b0[i] == b0[i - 1] and b1[j] == b1[j - 1]:
                    cache[i + 1, j + 1] = min(
                        cache[i - 1, i - 1] + 1,
                        cache[i + 1, j + 1])
    return cache[m, n]


@njit(nb.int32(NumbaBytesType, NumbaBytesType))
def jit_lsc_similarity(b0: NumbaBytesType, b1: NumbaBytesType) -> nb.int32:
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


def fast_lsc_similarity(s0: str, s1: str, encoding='utf-8') -> int:
    return jit_lsc_similarity(s0.encode(encoding), s1.encode(encoding))


def fast_hamming_distance(s0: str, s1: str, encoding="utf-8") -> int:
    return jit_hamming_distance(s0.encode(encoding), s1.encode(encoding))


if __name__ == '__main__':
    print(fast_edit_distance("abcfd", "acbfd"))
    print(fast_lsc("tr l", "trs l"))
    print(fast_hamming_distance("abcd", "abcdef"))
