
m = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3]
]


def opt_dist(m):
    row, col = len(m[0]), len(m)
    cache = [[0] * col for _ in range(row)]
    cache[0][0] = m[0][0]
    for i in range(row-1):
        cache[i+1][0] = cache[i][0] + m[i+1][0]
    for i in range(col-1):
        cache[0][i+1] = cache[0][i] + m[0][i+1]

    for i in range(1, row):
        for j in range(1, col):
            cache[i][j] = min(cache[i][j-1], cache[i-1][j]) + m[i][j]

    i, j = row-1, col-1
    path = []
    while i > 0 or j > 0:
        options = []
        if i > 0:
            options.append((cache[i-1][j], 0))
        if j > 0:
            options.append((cache[i][j-1], 1))

        if len(options) > 1 and options[0] > options[1]:
            options[0], options[1] = options[1], options[0]

        if options[0][1] == 0:
            path.append('down')
            i -= 1
        else:
            path.append('right')
            j -= 1

    for row in cache:
        print(row)
    path.reverse()
    print(path)





    # for row in cache:
    #     print(row)

if __name__ == '__main__':
    opt_dist(m)