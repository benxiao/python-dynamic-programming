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


def dp_edit_dist_custom(s0: str, s1: str):
    m, n = len(s0), len(s1)
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        cache[i][0] = i

    for j in range(n + 1):
        cache[0][j] = j

    for i, c0 in enumerate(s0):
        for j, c1 in enumerate(s1):
            insert_into = cache[i][j + 1] + \
                          (0.5 if (i > 0 and s0[i-1] == s0[i]) else 1)
            delete_from = cache[i + 1][j] + \
                          (0.5 if (j > 0 and s1[j-1] == s1[j]) else 1)

            match = cache[i][j] if c0 == c1 else cache[i][j] + (0.75 if (i == j) else 1)
            cache[i+1][j+1] = min([insert_into, delete_from, match])

    for row in cache:
        print(row)
    return cache[m][n]


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

    for row in cache:
        print(row)

    return cache[m][n]



if __name__ == '__main__':
    print(dp_edit_dist_custom("david", "maddison"))
    print(dp_edit_dist("maddison", "madison"))