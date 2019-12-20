"""
Longest repeated sequence

"""

seq = "ATACTCGGA"


def navie_lrs(seq, i, j):
    if i < 0 or j < 0:
        return 0

    if i!=j and seq[i] == seq[j]:
        return navie_lrs(seq, i-1, j-1) + 1

    return max(navie_lrs(seq, i-1, j), navie_lrs(seq, i,j-1))


def lrs(seq):
    l = len(seq)
    cache = [[0] * (l+1) for _ in range(l+1)]
    for i, c0 in enumerate(seq):
        for j, c1 in enumerate(seq):
            if i!=j and c0 == c1:
                cache[i+1][j+1] = cache[i][j] + 1
            else:
                cache[i+1][j+1] = max(cache[i][j+1], cache[i+1][j])
    return cache[l][l]


if __name__ == '__main__':
    print(navie_lrs(seq, len(seq)-1, len(seq)-1))
    print(lrs(seq))
