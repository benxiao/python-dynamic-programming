array = [7, 3, 2, 5, 8]
s = 14


# naive version
def subset_sum(array, n, i):
    if i < 0:
        return False

    exclude_path = subset_sum(array, n, i-1)
    if n - array[i] >= 0:
        if n == array[i]:
            return True

        include_path = subset_sum(array, n-array[i], i-1)
        return include_path or exclude_path
    return exclude_path


def dp_subset_sum(array, n):
    cache = [[False] * (n+1) for _ in range(len(array)+1)]
    for i in range(len(array)+1):
        cache[i][0] = True
    print(cache)
    for i, e in enumerate(array):
        for j in range(1, n+1):
            if j < array[i]:
                cache[i+1][j] = cache[i][j]
            else:
                cache[i+1][j] = cache[i][j] or cache[i][j-array[i]]

    return cache


if __name__ == '__main__':
    print(subset_sum(array, 14, len(array)-1))
    print(dp_subset_sum(array, 14))
