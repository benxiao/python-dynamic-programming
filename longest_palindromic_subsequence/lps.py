def lps(seq, i, j):
    if i == j:
        return 1

    if seq[i] == seq[j]:
        return lps(seq, i+1, j-1) + 2
    else:
        return max(lps(seq, i, j-1), lps(seq, i+1, j))


def dp_lps(seq):
    l = len(seq)
    cache = [[0] * l for _ in range(l)]
    for i in range(l):
        cache[i][i] = 1

    for i in range(1, l):
        for j in range(0, l-i):
            start, end = j, i+j
            if seq[start] == seq[end]:
                cache[start][end] = 2 + (cache[start+1][end-1] if end-1 >= start+1 else 0)
            else:
                cache[start][end] = max(cache[start+1][end], cache[start][end-1])
    return cache[0][l-1]


if __name__ == '__main__':
    # print(lps("abcbab", 0, 5))
    print(dp_lps("abcbab"))
