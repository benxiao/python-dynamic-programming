from functools import lru_cache


@lru_cache(maxsize=None)
def _lis(seq, i, m):
    if i < 0:
        return 0
    dont_take = _lis(seq, i - 1, m)
    if m >= seq[i]:
        take = _lis(seq, i - 1, seq[i]) + 1
        return max(dont_take, take)
    return dont_take


def lis(seq):
    return _lis(seq, len(seq)-1, max(seq))


if __name__ == '__main__':
    print(lis([1,2,10, 3,5, 6]))