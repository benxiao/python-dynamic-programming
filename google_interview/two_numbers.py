def navie_tn(array, target):
    l = len(array)
    for i in range(l-1):
        for j in range(i+1, l):
            if array[i] + array[j] == target:
                return i, j
    return None


def bisect_right(a, x, lo=0, hi=None, key=lambda x:x):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < key(a[mid]): hi = mid
        else: lo = mid+1
    return lo


def better_tn(array, target):
    l = len(array)
    argsorted = sorted(range(l), key=lambda x: array[x])
    for i, k in zip(range(l-1), argsorted):
        left = target - array[k]
        j = bisect_right(argsorted, left, i+1, key=lambda x: array[x])-1
        if j > i and array[argsorted[j]] == left:
            return k, argsorted[j]
    return None

print(better_tn([1,2,3,7,8], 6))


def fast_tn(array, target):
    available = {k: i for i, k in enumerate(array)}
    for i, k in enumerate(array):
        if target-k in available and i != available[target-k]:
            return i, available[target-k]
    return None


print(fast_tn([1,2,3,7,8], 15))


def rotate_array(lst, k):
    l = len(lst)
    if k >= l:
        raise ValueError()

    return lst[k:] + lst[:k]

if __name__ == '__main__':
    print(rotate_array([1,2,3,4,5,6], 3))