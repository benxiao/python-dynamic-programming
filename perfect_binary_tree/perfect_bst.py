from numba import njit
import numba as nb
import numpy as np


np.random.seed(42)

symbols = ["A", "B", "C"]
freqs = np.random.randint(5, 1000, 100)

Numba1DArray = nb.typeof(np.array([1]))
Numba2DArray = nb.typeof(np.array([[1]]))
print(Numba2DArray)


class TreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left = None
        self.right = None

    def __str__(self):
        return f"({self.left}<{self.symbol}>{self.right})"

    __repr__ = __str__


@njit(Numba2DArray(Numba1DArray))
def jit_dp_opt_bst(freqs: Numba1DArray)->Numba2DArray:
    n = len(freqs)
    cache = np.zeros((n, n))
    roots = np.full((n, n), -1)
    for i in range(n):
        cache[i, i] = freqs[i]

    for i in range(n):
        roots[i, i] = i

    dummy_max = np.iinfo(np.int64).max

    for k in range(1, n):
        for start in range(n-k):
            current_min = dummy_max
            current_idx_min = -1
            end = start + k
            for i in range(start, end+1):
                left_subtree = cache[start, i-1] if i-1 >= start else 0
                right_subtree = cache[i+1, end] if end >= i+1 else 0
                current = left_subtree + right_subtree + freqs[start:end+1].sum()
                if current < current_min:
                    current_min = current
                    current_idx_min = i
            roots[start, end] = current_idx_min
            cache[start, end] = current_min
    return roots


def dp_opt_bst(freqs):
    n = len(freqs)
    cache = [[0] * n for _ in range(n)]
    roots = [[None] * n for _ in range(n)]
    for i in range(n):
        cache[i][i] = freqs[i]

    for i in range(n):
        roots[i][i] = i

    for k in range(1, n):
        for start in range(n-k):
            current_min = float("inf")
            current_idx_min = -1
            end = start + k
            for i in range(start, end+1):
                left_subtree = cache[start][i-1] if i-1 >= start else 0
                right_subtree = cache[i+1][end] if end >= i+1 else 0
                current = left_subtree + right_subtree + sum(freqs[start:end+1])
                if current < current_min:
                    current_min = current
                    current_idx_min = i
            roots[start][end] = current_idx_min
            cache[start][end] = current_min
    return cache, roots


def opt_bst(freq, i, j, level):
    if j <= i:
        return 0, None

    min_value = len(freq) * sum(freq)
    min_tree = None
    for idx in range(i, j):
        left_value, left_tree = opt_bst(freq, i, idx, level + 1)
        right_value, right_tree = opt_bst(freq, idx + 1, j, level + 1)
        current = left_value + freq[idx] * level + right_value
        if current < min_value:
            min_value = current
            min_tree = TreeNode(symbols[idx])
            min_tree.left = left_tree
            min_tree.right = right_tree
    return min_value, min_tree


if __name__ == '__main__':
    #print(opt_tree(freq, 0, 3, 1))
    print(jit_dp_opt_bst(np.array(freqs)))
    #print(opt_bst(freqs, 0, 3, 0))