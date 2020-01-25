"""
** Coin change problem (total number of ways to get the denomination of coins **

Given an unlimited supply of coins of given denominations, find the total number of
distinct ways to get a desired change.
"""



lst = [1, 3, 5, 7]
import bisect


def total(n, lst, i):
    if n == 0:
        return [[]]
    result = []
    for k in range(i, len(lst)):
        if n-lst[k] >= 0:
            prev_result = total(n-lst[k], lst, k)
            for item in prev_result:
                item.append(lst[k])
            result.extend(prev_result)
    return result


def dp_total(n, lst):
    cache = [0] * (n+1)
    cache[0] = 1
    cache_items = [[] for _ in range(n+1)]
    cache_items[0].append([])
    for k in range(1, n+1):
        for c in lst:
            if k - c >= 0:
                for e in cache_items[k - c]:
                    if e and e[-1] > c:
                        continue
                    cache_items[k].append([*e, c])
                    cache[k] += 1

    return cache, cache_items


def flatten(xs):
    for x in xs:
        if isinstance(x, list):
            for xx in flatten(x):
                yield xx
        else:
            yield x


def dedupe(xs):
    lst = sorted(xs)
    if len(lst) < 2:
        return lst
    cur = xs[0]
    result = []
    for x in xs[1:]:
        if cur != x:
            result.append(cur)
            cur = x
    if result[-1] != cur:
        result.append(cur)
    return result


if __name__ == '__main__':
    print(dedupe([1, 2, 4, 5]))
