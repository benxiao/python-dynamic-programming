import numba as nb
import numpy as np
from constant import NB_BYTES, NB_1D_INT64_ARRAY


@nb.njit(NB_1D_INT64_ARRAY(NB_BYTES), fastmath=True)
def jit_z_algo(source):
    source_length = len(source)
    z_values = np.zeros(source_length, dtype=nb.int64)
    left, right = 0, 0
    for k in range(1, source_length):
        # we do str cmp
        if k >= right:
            left = right = k
            for i, j in enumerate(range(k, source_length)):
                if source[i] != source[j]:
                    break
                right += 1

            z_values[k] = right - left

        # we may use the precomputed results
        else:
            z_value = z_values[k-left]
            # we stay within the current zbox
            if k + z_value < right:
                z_values[k] = z_value

            # we extend outside the current zbox
            else:
                # length within the zbox
                length = right - k
                while k+length < source_length:
                    if source[length] != source[k+length]:
                        break
                    length += 1
                z_values[k] = length
                left = k
                right = left + length
    return z_values


def z_algo(source):
    return jit_z_algo(source.encode()).tolist()

