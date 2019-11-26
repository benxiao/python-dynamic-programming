def lsc(s0, s1):
    cache = [[0] * (len(s1)+1) for _ in range(len(s0)+1)]
    for i, c0 in enumerate(s0):
        for j, c1 in enumerate(s1):
            if c0 == c1:
                cache[i+1][j+1] = cache[i][j] + 1
            else:
                cache[i+1][j+1] = max(
                    cache[i][j+1],
                    cache[i+1][j],
                )

    print(cache)


if __name__ == '__main__':
    lsc("AGGTAB", "GXTXAYB")