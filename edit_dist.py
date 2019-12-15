def recur_edit_dist(s0, s1, m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    if s0[m] == s1[n]:
        return recur_edit_dist(s0, s1, m - 1, n - 1)

    return 1 + min(
        recur_edit_dist(s0, s1, m, n - 1),
        recur_edit_dist(s0, s1, m - 1, n),
        recur_edit_dist(s0, s1, m - 1, n - 1)
    )


def dp_edit_dist(s0: str, s1: str):
    m, n = len(s0), len(s1)
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        cache[i][0] = i

    for j in range(n + 1):
        cache[0][j] = j

    for i, c0 in enumerate(s0):
        for j, c1 in enumerate(s1):
            if c0 == c1:
                cache[i + 1][j + 1] = cache[i][j]
            else:
                cache[i + 1][j + 1] = 1 + min(
                    cache[i][j + 1],  # insert
                    cache[i + 1][j],  # delete
                    cache[i][j]  # replace
                )

    return cache[m][n]





if __name__ == '__main__':
    print(dp_edit_dist("abcde", "a"))
    print(fast_edit_distance("abcde", "a"))