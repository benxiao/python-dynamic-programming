"""
Increasing Subsequence with Maximum Sum

Find a subsequence of a given sequence such that subsequence sum is
as high as possible and subsequence's elements are in sorted order, from lowest
to highest.This subsequence is not necessarily contiguous, or unique

"""


a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]

def lsis_simple(a):
    l = len(a)
    cache = [0] * (len(a)+1)
    cache[1] = a[0]
    current_max = 0
    for i in range(2, l+1):
        for j in reversed(range(1, i)):
            if a[i-1] > a[j-1]:
                cache[i] = max(cache[i], cache[j]+a[i-1])
                if cache[i] > current_max:
                    current_max = cache[i]
    return current_max


def lsis_simple_with_result(a):
    l = len(a)
    cache = [0] * (l + 1)
    cache[1] = a[0]
    cache_items = [None] * (l + 1)
    cache_items[1] = [a[0]]
    max_idx = 0
    for i in range(2, l + 1):
        for j in reversed(range(1, i)):
            if a[i - 1] > a[j - 1]:
                if cache[j] + a[i-1] > cache[i]:
                    cache[i] = cache[j] + a[i-1]
                    cache_items[i] = [*cache_items[j], a[i-1]]
        if cache[i] > cache[max_idx]:
            max_idx = i

    print(cache, cache_items)
    return cache_items[max_idx]





if __name__ == '__main__':
    print(lsis_simple(a))
    print(lsis_simple_with_result(a))
