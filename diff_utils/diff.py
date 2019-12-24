
def diff_two_files(fn0: str, fn1: str):
    with open(fn0) as fp0, open(fn1) as fp1:
        lines0 = [line for line in fp0]
        lines1 = [line for line in fp1]

    m, n = len(lines0), len(lines1)
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        cache[i][0] = i

    for j in range(n + 1):
        cache[0][j] = j

    for i, c0 in enumerate(lines0):
        for j, c1 in enumerate(lines1):
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
        if i > 0 and j > 0 and lines0[i-1] == lines1[j-1]:
            options.append(((i-1, j-1),
                            cache[i-1][j-1],
                            f" {lines0[i-1]}"
                            ))
        if i > 0:
            options.append(((i-1, j),
                            cache[i-1][j],
                            f"(-) {lines0[i - 1]}"
                            ))
        if j > 0:
            options.append(((i, j-1),
                            cache[i][j-1],
                            f"(+) {lines1[j - 1]}"
                            ))
        best_options = min(options, key=lambda x: x[1])
        i, j = best_options[0]
        result.append(best_options[2])

    result = list(reversed(result))
    for line in result:
        print(line, end='')
    print(end='\n'*2)


if __name__ == '__main__':
    import sys
    _, fn0, fn1 = sys.argv
    diff_two_files(fn0, fn1)
