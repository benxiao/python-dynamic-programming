from typing import *
import numba as nb
import numpy as np
from timeit import timeit

def coins(n: int, choices: List):
    array = [0] * (n + 1)
    for i in range(1, n + 1):
        min_l = n  # worst case and used it as a placeholder
        for choice in choices:
            if i - choice >= 0:
                if array[i - choice] + 1 < min_l:
                    min_l = array[i - choice] + 1
        array[i] = min_l
    return array[n]


def coins_opt(n: int, choices: List):
    array = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        min_l, items = n, []
        for choice in choices:
            if i - choice >= 0:
                if len(array[i - choice]) + 1 < min_l:
                    min_l = len(array[i - choice]) + 1
                    items = array[i - choice] + [choice]  # this creates a list, so don't worry
        array[i] = items
    return array[n]


Numba1DArray = nb.typeof(np.array([1]))


@nb.njit(nb.int32(nb.int32, Numba1DArray))
def jit_coins(n: int, choices: Numba1DArray)->nb.int32:
    array = np.zeros(n + 1)
    for i in range(1, n + 1):
        min_l = n  # worst case and used it as a placeholder
        for choice in choices:
            if i - choice >= 0:
                if array[i - choice] + 1 < min_l:
                    min_l = array[i - choice] + 1
        array[i] = min_l
    return array[n]


def fast_coins(n: int, choices: List):
    return jit_coins(n, np.array(choices))


print(coins_opt(12, [1, 5, 7, 10]))
print(jit_coins(12, np.array([1, 5, 7, 10])))