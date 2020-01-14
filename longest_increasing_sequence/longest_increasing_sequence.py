from functools import lru_cache


def _lis(seq, i, m):
    if i < 0:
        return 0
    dont_take = _lis(seq, i - 1, m)
    if m > seq[i]:
        take = _lis(seq, i - 1, seq[i]) + 1
        return max(dont_take, take)
    return dont_take


def lis_simple(a):
    l = len(a)
    cache = [0] * (len(a)+1)
    cache[1] = 1
    current_max = 0
    for i in range(2, l+1):
        for j in reversed(range(1, i)):
            if a[i-1] > a[j-1]:
                cache[i] = max(cache[i], cache[j]+1)
                if cache[i] > current_max:
                    current_max = cache[i]
    return current_max


def lis_simple_with_result(a):
    l = len(a)
    cache = [0] * (l + 1)
    cache[1] = 1
    cache_items = [None] * (l + 1)
    cache_items[1] = [a[0]]
    max_idx = 0
    for i in range(2, l + 1):
        for j in reversed(range(1, i)):
            if a[i - 1] > a[j - 1]:
                if cache[j] + 1 > cache[i]:
                    cache[i] = cache[j] + 1
                    cache_items[i] = [*cache_items[j], a[i-1]]
        if cache[i] > max_idx:
            max_idx = cache[i]

    return cache_items[max_idx]


def _lis_result(seq, i, m):
    if i < 0:
        return 0, []
    dont_take = _lis_result(seq, i - 1, m)
    dont_take_val, dont_take_result = dont_take
    if m > seq[i]:
        take = _lis_result(seq, i-1, seq[i])
        take_val, take_result = take
        take_val = take_val + 1
        take_result = take_result + [seq[i]]
        if take_val > dont_take_val:
            return take_val, take_result
    return dont_take


def lis(seq):
    return _lis(seq, len(seq) - 1, max(seq) + 1)


def lis_result(seq):
    return _lis_result(seq, len(seq)-1, max(seq)+1)


if __name__ == '__main__':
    lst = [1, 2, 10, 11, 12, 3, 5]
    sorted(lst)

    print(lis_simple(lst))
    print(lis_simple_with_result(lst))
    print(lis(lst))
    print(lis_result(lst))
