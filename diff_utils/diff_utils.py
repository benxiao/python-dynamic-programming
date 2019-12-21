
def dp_diff_utils(s0: str, s1: str):
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
                )

    i, j = m, n
    result = []
    while i > 0 or j > 0:
        options = []
        if i > 0 and j > 0 and s0[i-1] == s1[j-1]:
            options.append(((i-1, j-1),
                            cache[i-1][j-1],
                            s0[i-1]
                            ))
        if i > 0:
            options.append(((i-1, j),
                            cache[i-1][j],
                            f"(-{s0[i - 1]})"
                            ))
        if j > 0:
            options.append(((i, j-1),
                            cache[i][j-1],
                            f"(+{s1[j - 1]})"
                            ))
        best_options = min(options, key=lambda x: x[1])
        i, j = best_options[0]
        result.append(best_options[2])

    return cache[m][n], "".join(reversed(result))


if __name__ == "__main__":
    print(dp_diff_utils("abcd", "acd"))