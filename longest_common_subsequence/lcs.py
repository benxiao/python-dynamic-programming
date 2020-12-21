from itertools import chain, repeat


def lcs(s0, s1):
    m, n = len(s0), len(s1)
    cache = [[0] * (n+1) for _ in range(m+1)]
    for i, c0 in enumerate(s0):
        for j, c1 in enumerate(s1):
            if c0 == c1:
                cache[i+1][j+1] = cache[i][j] + 1
            else:
                if cache[i][j+1] > cache[i+1][j]:
                    cache[i+1][j+1] = cache[i][j+1]
                else:
                    cache[i+1][j+1] = cache[i+1][j]

    # track number of continous insertions
    i, j = m, n
    cuts_left = [0] * m
    cuts_right = [0] * n
    while i > 0 and j > 0:
        # if two characters match
        if cache[i][j] > cache[i-1][j-1] and s0[i-1] == s1[j-1]:
            i -= 1
            j -= 1
        # if two characters mismatch, we follow the path where cache[..][..] and cache[..][..]
        # have the same longest common subsequence
        elif cache[i][j] == cache[i-1][j]:
            i -= 1
            cuts_right[j-1] += 1
        elif cache[i][j] == cache[i][j-1]:
            j -= 1
            cuts_left[i-1] += 1

    while i > 0:
        i -= 1
        cuts_right[j] = 1

    while j > 0:
        j -= 1
        cuts_left[i] = 1

    print(cuts_left)
    print(cuts_right)

    return [(which, pos, cut) for which, pos, cut
            in chain(zip(repeat('l'), range(m), cuts_left),
                     zip(repeat('r'), range(n), cuts_right))
            if cut > 0], cache[m][n]


if __name__ == '__main__':
    # perfect usecase for messy data
    print(lcs("trucson le", "truc le"))
    print()
    print(lcs("melone", "melbourne"))