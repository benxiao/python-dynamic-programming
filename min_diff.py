a = [2, 4, 13, 10, 1]
a1 = [10, 1, 2, 4, 13]

# try to divide the array into two partitions as balanced as possible.

# without caching
def recur_min_diff(array, n):
    if n < 0:
        return 0, [], []

    diff, p0, p1 = recur_min_diff(array, n - 1)
    left = diff+array[n], p0+[array[n]], p1
    right = diff-array[n], p0, p1+[array[n]]

    if abs(left[0]) > abs(right[0]):
        return right
    return left


# dynamic programming
def dp_min_diff(array):
    l = len(array)
    cache = [0] * (l+1)
    cache_items = [[[], []] for _ in range(l+1)]
    for i, e in enumerate(array):
        p0, p1 = cache_items[i]
        pleft = cache[i] + e
        pright = cache[i] - e
        if abs(pleft) < abs(pright):
            cache[i+1] = pleft
            cache_items[i+1] = [p0 + [e], p1]
        else:
            cache[i+1] = pright
            cache_items[i + 1] = [p0, p1 + [e]]
    return cache[l], cache_items[l]


if __name__ == '__main__':
    print(recur_min_diff(a, len(a) - 1))
    print(dp_min_diff(a))
