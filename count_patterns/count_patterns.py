from functools import lru_cache

source = "subsequence"
pattern = "sue"


@lru_cache(maxsize=None)
def count_patterns(source, pattern, m, n):
    if n == -1:
        return 1, [[]]

    if m == -1:
        return 0, []

    if source[m] == pattern[n]:
        i0, r0 = count_patterns(source, pattern, m-1, n-1)
        r0 = [r+[m] for r in r0]
    else:
        i0, r0 = 0, []

    i1, r1 = count_patterns(source, pattern, m-1, n)
    return i0 + i1, r0 + r1


if __name__ == '__main__':
    print(count_patterns(source, pattern, len(source)-1, len(pattern)-1))