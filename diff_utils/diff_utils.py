
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
                            f" {s0[i-1]}"
                            ))
        if i > 0:
            options.append(((i-1, j),
                            cache[i-1][j],
                            f"-{s0[i - 1]}"
                            ))
        if j > 0:
            options.append(((i, j-1),
                            cache[i][j-1],
                            f"+{s1[j - 1]}"
                            ))
        best_options = min(options, key=lambda x: x[1])
        i, j = best_options[0]
        result.append(best_options[2])

    result = list(reversed(result))
    joined_result = []
    for sign , ch in result:
        if joined_result:
            prev = joined_result.pop()
            prev_sign = prev[0]
            if prev_sign == sign:
                joined_result.append(prev+ch)
            else:
                joined_result.append(prev)
                joined_result.append(sign+ch)

        else:
            joined_result.append(sign+ch)

    joined_result = [x[1:] if x.startswith(" ") else x for x in joined_result]
    joined_result = [f"({x})" if x[0] in ("+", "-") else x for x in joined_result]
    return "".join(joined_result)


if __name__ == "__main__":
    print(dp_diff_utils("Janelle", "Jenalle"))