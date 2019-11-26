array = [7, 3, 2, 5, 8]
s = 14

# naive version
def subset(array, n, i):
    if i < 0:
        return False

    exclude_path = subset(array, n, i-1)
    if n - array[i] >= 0:
        if n == array[i]:
            return True

        include_path = subset(array, n-array[i], i-1)
        return include_path or exclude_path
    return exclude_path


def dp_subset(array, n, i):
    pass


if __name__ == '__main__':
    print(subset(array, 24, len(array)-1))
