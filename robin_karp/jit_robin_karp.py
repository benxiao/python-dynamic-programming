import numba as nb
import numpy as np

NumbaBytes = nb.typeof("".encode())
Numba1dIntArray = nb.typeof(np.array([1], dtype=np.int64))


@nb.njit(Numba1dIntArray(NumbaBytes, NumbaBytes), fastmath=True)
def jit_robin_karp(text, pattern):
    length_text = len(text)
    length_pattern = len(pattern)
    prime = 83921
    hash_pattern = 0
    hash_text = 0
    d = 256
    h = 1
    for _ in range(length_pattern-1):
        h = (h * d) % prime

    for x, y in zip(pattern, text):
        hash_pattern = (hash_pattern * d + x) % prime
        hash_text = (hash_text * d + y) % prime

    result = []
    i, j = 0, length_pattern
    while 1:
        if hash_text == hash_pattern:
            for ii, jj in zip(range(length_pattern), range(i, i+length_pattern)):
                if pattern[ii] != text[jj]:
                    break
            else:
                result.append(i)

        if j == length_text:
            break

        # sliding
        hash_text = ((hash_text - h * text[i]) * d + text[j]) % prime
        i += 1
        j += 1

    return np.array(result)


if __name__ == '__main__':
    print(jit_robin_karp.inspect_types())