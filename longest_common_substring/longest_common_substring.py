from typing import *

x = "xxbcdxyz"
y = "xyzabcde"


def longest_common_substring(s0: str, s1: str) -> Tuple[int, int]:
    """
    :param s0: first string
    :param s1: second string
    :return: length of the max substring, and the index of its first character from s0
    """
    l0, l1 = len(s0), len(s1)

    # cache
    result, idx = 0, 0
    cache = [[0] * (l1 + 1) for _ in range(l0 + 1)]

    for i in range(1, l0 + 1):
        for j in range(1, l1 + 1):
            if s0[i - 1] == s1[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
                if cache[i][j] > result:
                    result = cache[i][j]
                    idx = i
            else:
                cache[i][j] = 0
    return result, idx - result


if __name__ == '__main__':
    print(longest_common_substring(x, y))
    print(longest_common_substring("Christine", "Kristine"))
